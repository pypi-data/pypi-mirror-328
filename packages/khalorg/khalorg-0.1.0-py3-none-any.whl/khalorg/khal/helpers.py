import logging
import sys
from datetime import date, datetime
from os.path import dirname, exists, join
from subprocess import STDOUT, CalledProcessError, check_output
from typing import Callable

from khalorg import paths

Time = date | datetime


def find_khal_bin() -> str:
    """Returns the khal executable.

    When pipx is used, the khal executable is located in the same directory
    as the python executable. When using a virtual environment, or the
    global python installation, the khal executable is located in the PATH.

    Returns:
    --------
        path to the khal executable
    """
    bin: str = join(dirname(sys.executable), "khal")
    bin = bin if exists(bin) else "khal"
    logging.debug("khal executable is: %s", bin)
    return bin


def get_khal_format():
    """
    Returns the format that is used for the `khal list --format` command
    that is used within the `khalorg list` command.

    Returns
    -------
        the khal list format

    """
    with open(paths.khal_format) as file_:
        return file_.read()


def is_future(timestamp: datetime | date) -> bool:
    """
    Whether the `timestamp` is in the future.

    Args:
    ----
        timestamp: the time

    Returns:
    -------
        True if the `timestamp` is in the future

    """
    logging.debug("Check if timestamp %s is in the future", timestamp)
    if isinstance(timestamp, datetime):
        logging.debug(
            "Timestamp is a datetime object with tzinfo %s", timestamp.tzinfo
        )
        now = datetime.now(timestamp.tzinfo)
    else:
        now = datetime.now().date()

    logging.debug("Now is %s", now)
    return timestamp >= now


def subprocess_callback(cmd: list) -> Callable:
    """
    Returns a subprocess.check_output callback where the `cmd` is defined
    beforehand.

    Args:
    ----
        cmd: the base command. For example: ['khal', 'new']

    Returns:
    -------
        callback function

    """

    def callback(args: list) -> str:
        return try_check_output([*cmd, *args]).decode()

    return callback


def try_check_output(args: list) -> bytes:
    try:
        return check_output(args, stderr=STDOUT)
    except CalledProcessError as error:
        error_message: str = (
            f"The following arguments were sent to khal:\n\n{' '.join(args)}"
            "\n\nNext, the following error was received from khal:\n\n"
            f"{error.output.decode()}\n\n"
        )
        logging.critical(error_message)
        raise Exception(error_message) from error


def remove_tzinfo(time: Time) -> Time:
    """
    Remove tzinfo if possible.

    Args:
    ----
        time: a date of a datetime object

    Returns:
    -------
        `time` without an updated tzinfo if possible

    """
    return time.replace(tzinfo=None) if isinstance(time, datetime) else time


def set_tzinfo(time: Time, timezone) -> Time:
    """
    Add tzinfo if possible.

    Args:
    ----
        time: a date of a datetime object
        tzinfo: timezone as str

    Returns:
    -------
        `time` with an updated tzinfo if possible

    """
    return timezone.localize(time) if isinstance(time, datetime) else time
