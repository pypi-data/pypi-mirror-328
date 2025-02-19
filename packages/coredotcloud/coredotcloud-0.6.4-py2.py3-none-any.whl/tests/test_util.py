import pytest

from click.testing import CliRunner

# from coredotcloud import coredotcloud
from coredotcloud.util import *

import datetime
from pytz import timezone


def test_get_datetime_now():
    assert type(get_datetime_now()) == datetime.datetime
    assert type(get_datetime_now(add_hours=1)) == datetime.datetime
    assert type(get_datetime_now(add_hours=9)) == datetime.datetime
    assert type(get_datetime_now(add_hours=0)) == datetime.datetime
    assert type(get_datetime_now(add_hours=-1)) == datetime.datetime
    assert get_datetime_now(add_hours=1) > get_datetime_now()
    assert get_datetime_now(add_hours=-1) < get_datetime_now()


def test_convert_datetime_time():
    assert convert_datetime_time(datetime.datetime.now())
    assert int(convert_datetime_time(datetime.datetime.now())) > 0


def test_get_seoul_time_now():
    assert get_seoul_time_now()
    assert type(get_seoul_time_now()) == float
    assert get_seoul_time_now(is_datetime=1)
    assert type(get_seoul_time_now(is_datetime=1)) == datetime.datetime
    assert datetime.datetime.now(
        timezone('Asia/Seoul')).hour == get_seoul_time_now(is_datetime=1).hour
