# Simple commands for controling the mako sub.
# Grabbed from the examples
from time import sleep

from eyepy.motors import MOTORDrive

MAKO_PSD_FRONT = 1
MAKO_PSD_FRONT_LEFT = 2
MAKO_PSD_FRONT_RIGHT = 3
MAKO_PSD_BACK_LEFT = 4
MAKO_PSD_BACK_RIGHT = 5
MAKO_PSD_DOWN = 6

# Thruster IDs.
MAKO_LEFT = 1
MAKO_FRONT = 2
MAKO_RIGHT = 3
MAKO_BACK = 4


def up(secs: int, speed: int = 100) -> None:
    """Blocking drive the sub up at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_FRONT, speed)
    MOTORDrive(MAKO_BACK, speed)
    sleep(secs)
    MOTORDrive(MAKO_FRONT, 0)
    MOTORDrive(MAKO_BACK, 0)


def down(secs: int, speed: int = 100) -> None:
    """Blocking drive the sub down at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_FRONT, -speed)
    MOTORDrive(MAKO_BACK, -speed)
    sleep(secs)
    MOTORDrive(MAKO_FRONT, 0)
    MOTORDrive(MAKO_BACK, 0)


def forwards(secs: int, speed: int = 100) -> None:
    """Blocking drive the sub fowards at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_LEFT, speed)
    MOTORDrive(MAKO_RIGHT, speed)
    sleep(secs)
    MOTORDrive(MAKO_LEFT, 0)
    MOTORDrive(MAKO_RIGHT, 0)


def backwards(secs: int, speed: int = 100) -> None:
    """Blocking drive the sub backwards at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_LEFT, -speed)
    MOTORDrive(MAKO_RIGHT, -speed)
    sleep(secs)
    MOTORDrive(MAKO_LEFT, 0)
    MOTORDrive(MAKO_RIGHT, 0)


def turn_left(secs: int, speed: int = 100) -> None:
    """Blocking turn the sub left at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_LEFT, -speed)
    MOTORDrive(MAKO_RIGHT, speed)
    sleep(secs)
    MOTORDrive(MAKO_LEFT, 0)
    MOTORDrive(MAKO_RIGHT, 0)


def turn_right(secs: int, speed: int = 100) -> None:
    """Blocking turn the sub right at `speed` for `secs`

    Parameters
    ----------
    secs : int
        Number of seconds to drive the sub for
    speed : int
        The speed to drive the sub for. Defaults to 100

    """
    MOTORDrive(MAKO_LEFT, speed)
    MOTORDrive(MAKO_RIGHT, -speed)
    sleep(secs)
    MOTORDrive(MAKO_LEFT, 0)
    MOTORDrive(MAKO_RIGHT, 0)
