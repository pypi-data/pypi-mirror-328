import subprocess
from datetime import datetime

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from ..database.database import engine
from ..database.models import Mediaitem, ShareLimits
from .base import BaseService
from .config import appconfig
from .sse import SseEventFrontendNotification, SseService

TIMEOUT_PROCESS_RUN = 6  # command to print needs to complete within 6 seconds.


class ShareService(BaseService):
    """Handle all image related stuff"""

    def __init__(self, sse_service: SseService):
        super().__init__(sse_service)

        # common objects
        pass

        # custom service objects
        pass

    def start(self):
        super().start()
        pass
        super().started()

    def stop(self):
        super().stop()
        pass
        super().stopped()

    def share(self, mediaitem: Mediaitem, config_index: int = 0):
        """print mediaitem"""

        if not appconfig.share.sharing_enabled:
            self._sse_service.dispatch_event(
                SseEventFrontendNotification(
                    color="negative",
                    message="Share service is disabled! Enable in config first.",
                    caption="Share Service Error",
                )
            )
            raise ConnectionRefusedError("Share service is disabled! Enable in config first.")

        # get config
        try:
            action_config = appconfig.share.actions[config_index]
        except Exception as exc:
            self._logger.critical(f"could not find action configuration with index {config_index}, error {exc}")
            raise exc

        # check counter limit

        with Session(engine) as session:
            statement = select(ShareLimits).where(ShareLimits.action == action_config.name)
            results = session.scalars(statement)
            result = results.one_or_none()

        current_shares = result.count if result else 0
        last_used_at = result.last_used_at if result else None

        if self.is_quota_exceeded(current_shares, action_config.processing.max_shares):
            self._sse_service.dispatch_event(
                SseEventFrontendNotification(
                    color="negative",
                    message=f"{action_config.trigger.ui_trigger.title} quota exceeded ({action_config.processing.max_shares} maximum)",
                    caption="Share/Print quota",
                )
            )
            raise BlockingIOError("Maximum number of Share/Print reached!")

        # block queue new prints until configured time is over
        remaining_s = self.remaining_time_blocked(action_config.processing.share_blocked_time, last_used_at)
        if remaining_s > 0:
            self._sse_service.dispatch_event(
                SseEventFrontendNotification(
                    color="info",
                    message=f"Request ignored! Wait {remaining_s:.0f}s before trying again.",
                    caption="Share Service Error",
                )
            )
            raise BlockingIOError(f"Request ignored! Wait {remaining_s:.0f}s before trying again.")

        # filename absolute to print, use in printing command
        filename = mediaitem.processed.absolute()

        try:
            # print command
            self._logger.info(f"share/print {filename=}")

            self._sse_service.dispatch_event(
                SseEventFrontendNotification(
                    color="positive",
                    message=f"Process '{action_config.name}' started.",
                    caption="Share Service",
                    spinner=True,
                )
            )

            completed_process = subprocess.run(
                str(action_config.processing.share_command).format(filename=filename),
                capture_output=True,
                check=True,
                timeout=TIMEOUT_PROCESS_RUN,
                shell=True,  # needs to be shell so a string as command is accepted.
            )

            self._logger.info(f"cmd={completed_process.args}")
            self._logger.info(f"stdout={completed_process.stdout}")
            self._logger.debug(f"stderr={completed_process.stderr}")

            self._logger.info(f"command started successfully {mediaitem}")

        except Exception as exc:
            self._sse_service.dispatch_event(SseEventFrontendNotification(color="negative", message=f"{exc}", caption="Share/Print Error"))
            raise RuntimeError(f"Process failed, error {exc}") from exc

        updated_current_shares = self.limit_counter_increment(action_config.name)

        if action_config.processing.max_shares > 0:
            # quota is enabled.

            self._sse_service.dispatch_event(
                SseEventFrontendNotification(
                    color="info",
                    message=f"{action_config.trigger.ui_trigger.title} quota is {updated_current_shares} of {action_config.processing.max_shares}",
                    caption="Share/Print quota",
                )
            )

    def limit_counter_reset(self, field: str):
        try:
            with Session(engine) as session:
                statement = delete(ShareLimits).where(ShareLimits.action == field)
                result = session.execute(statement)
                session.commit()

                self._logger.info(f"deleted {result.rowcount} items from ShareLimits")

        except Exception as exc:
            raise RuntimeError(f"failed to reset {field}, error: {exc}") from exc

    def limit_counter_reset_all(self):
        try:
            with Session(engine) as session:
                statement = delete(ShareLimits)
                results = session.execute(statement)
                session.commit()
                self._logger.info(f"deleted {results.rowcount} entries from ShareLimits")

        except Exception as exc:
            raise RuntimeError(f"failed to reset ShareLimits, error: {exc}") from exc

    def limit_counter_increment(self, field: str) -> int:
        try:
            with Session(engine) as session:
                db_entry = session.get(ShareLimits, field)
                if not db_entry:
                    # add 0 to db
                    session.add(ShareLimits(action=field))

                statement = select(ShareLimits).where(ShareLimits.action == field)
                results = session.scalars(statement)
                result = results.one()
                result.count += 1
                result.last_used_at = datetime.now()
                session.add(result)
                session.commit()

                return result.count
        except Exception as exc:
            raise RuntimeError(f"failed to update ShareLimits, error: {exc}") from exc

    def is_quota_exceeded(self, current_shares: int, max_shares: int) -> bool:
        if max_shares > 0 and current_shares >= max_shares:
            return True
        else:
            return False

    def remaining_time_blocked(self, shall_block_time_s: int, last_used_at: datetime | None) -> float:
        if last_used_at is None:
            return 0.0

        delta = (datetime.now() - last_used_at).total_seconds()

        if delta >= shall_block_time_s:
            # last print is longer than configured time in the past - return 0 to indicate no wait time
            return 0.0
        else:
            # there is some time to wait left.
            return shall_block_time_s - delta

    def _print_timer_fun(self):
        ## thread to send updates to client about remaining blocked time
        pass
