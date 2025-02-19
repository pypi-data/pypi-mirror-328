import datetime
import time


def get_datetime_now(add_hours=0):
    """
    Now time based on utc(Coordinated Universal Time)

    Parameters
    ----------
    add_hours : int
        plus or minus local time
    timestamp : int
        datetime or time

    Returns
    -------
    datetime
        now
    """
    t = datetime.datetime.utcnow()
    if add_hours:
        t += datetime.timedelta(hours=add_hours)
    return t


def convert_datetime_time(t):
    """
    Convert timestamp

    Parameters
    ----------
    t : datetime

    Returns
    -------
    int
        timestamp
    """
    return datetime.datetime.timestamp(t)


def get_seoul_time_now(is_datetime=0):
    """
    Seoul time based on utc

    Parameters
    ----------
    is_datetime : int
        return value type

    Returns
    -------
    datetime or time by `is_datetime`

    """
    t = get_datetime_now(add_hours=9)
    if is_datetime:
        return t
    else:
        return convert_datetime_time(t)
