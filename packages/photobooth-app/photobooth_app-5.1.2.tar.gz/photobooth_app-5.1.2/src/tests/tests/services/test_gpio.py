import logging
import time
from unittest.mock import patch

import pytest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from photobooth.container import Container, container
from photobooth.services.config import appconfig
from photobooth.services.gpio import DEBOUNCE_TIME, HOLD_TIME_REBOOT, HOLD_TIME_SHUTDOWN

Device.pin_factory = MockFactory()
logger = logging.getLogger(name=None)


# need fixture on module scope otherwise tests fail because GPIO lib gets messed up
@pytest.fixture(scope="module")
def _container() -> Container:
    # setup

    # tests fail if not enabled
    appconfig.hardwareinputoutput.gpio_enabled = True

    container.start()

    # deliver
    yield container
    container.stop()


@patch("subprocess.check_call")
def test_button_shutdown(mock_check_call, _container: Container):
    # emulate gpio active low driven (simulates button press)
    _container.gpio_service.shutdown_btn.pin.drive_low()

    # wait hold time
    time.sleep(DEBOUNCE_TIME + HOLD_TIME_SHUTDOWN + 0.5)

    # check subprocess.check_call was invoked
    mock_check_call.assert_called()


@patch("subprocess.check_call")
def test_button_reboot(mock_check_call, _container: Container):
    # emulate gpio active low driven (simulates button press)
    _container.gpio_service.reboot_btn.pin.drive_low()

    # wait hold time
    time.sleep(DEBOUNCE_TIME + HOLD_TIME_REBOOT + 0.5)

    # check subprocess.check_call was invoked
    mock_check_call.assert_called()


def test_button_action_buttons(_container: Container):
    # modify config
    # services.config().hardwareinputoutput.gpio_enabled = True

    with patch.object(_container.processing_service, "_start_job"):
        # emulate gpio active low driven (simulates button press)
        for action_button in _container.gpio_service.action_btns:
            action_button.pin.drive_low()

            # wait debounce time
            time.sleep(DEBOUNCE_TIME + 0.5)

        _container.processing_service._start_job.assert_called()

        assert len(_container.gpio_service.action_btns) == _container.processing_service._start_job.call_count


@patch("subprocess.run")
def test_button_share(mock_run, _container: Container):
    appconfig.share.sharing_enabled = True

    # emulate gpio active low driven (simulates button press)
    for share_button in _container.gpio_service.share_btns:
        share_button.pin.drive_low()

        # wait debounce time
        time.sleep(DEBOUNCE_TIME + 0.5)

        # emulate print finished, to avoid need to wait for blocking time.
        _container.share_service._last_print_time = None

    mock_run.assert_called()

    assert len(_container.gpio_service.share_btns) == mock_run.call_count


def test_light_switched_during_process(_container: Container):
    # emulate gpio active low driven (simulates button press)

    pin: MockPin = _container.gpioout_service.light_out.pin
    pin.clear_states()

    _container.processing_service.trigger_action("image", 0)
    _container.processing_service.wait_until_job_finished()

    # could use also pin.assert_states but strict is false and so it would not fail if more states are present.
    for actual, expected in zip(pin.states, [True, False, True], strict=True):
        assert actual.state == expected


def test_light_switched_during_process_turn_off_after_capture(_container: Container):
    # emulate gpio active low driven (simulates button press)
    appconfig.hardwareinputoutput.gpio_light_off_after_capture = True

    pin: MockPin = _container.gpioout_service.light_out.pin
    pin.clear_states()

    _container.processing_service.trigger_action("collage", 0)
    _container.processing_service.wait_until_job_finished()

    # could use also pin.assert_states but strict is false and so it would not fail if more states are present.
    for actual, expected in zip(pin.states, [True, False, True, False, True], strict=True):
        assert actual.state == expected

    appconfig.hardwareinputoutput.gpio_light_off_after_capture = False
    pin.clear_states()

    _container.processing_service.trigger_action("collage", 0)
    _container.processing_service.wait_until_job_finished()

    # could use also pin.assert_states but strict is false and so it would not fail if more states are present.
    for actual, expected in zip(pin.states, [True, False, True], strict=True):
        assert actual.state == expected
