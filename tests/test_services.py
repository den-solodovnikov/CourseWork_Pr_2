import sys
from io import StringIO
from unittest.mock import patch

import pytest

from src.services import (filter_aeroplanes, get_aeroplanes_by_altitude,
                          sort_aeroplanes, get_top_aeroplanes, print_aeroplanes)


def test_filter_aeroplanes(aeroplanes_test):
    result = filter_aeroplanes([], [])
    assert result == []
    result = filter_aeroplanes(aeroplanes_test, ["Ireland", "Bulgaria"])
    assert len(result) == 3
    assert result == [
       {
            "code": "4caa53",
            "callsign": "EAI48D",
            "country_reg": "Ireland",
            "geo_altitude": 4503.42,
            "velocity": 150.72
        },
        {
            "code": "4caa54",
            "callsign": "EAI75B  ",
            "country_reg": "Ireland",
            "geo_altitude": 4091.94,
            "velocity": 100.84
        },
        {
            "code": "451cc1",
            "callsign": "LZB9067 ",
            "country_reg": "Bulgaria",
            "geo_altitude": 11666.22,
            "velocity": 215.05
        }
    ]


def test_get_aeroplanes_by_altitude(aeroplanes_test):
    result = get_aeroplanes_by_altitude(aeroplanes=[], altitude_range="1000-5000")
    assert result == []
    result = get_aeroplanes_by_altitude(aeroplanes_test, altitude_range="")
    assert result == []
    result = get_aeroplanes_by_altitude(aeroplanes_test, altitude_range="1000 - 5000")
    assert len(result) == 2


# def test_get_aeroplanes_by_altitude_raise(aeroplanes_test):
#     with pytest.raises(IndexError):
#         result = get_aeroplanes_by_altitude(aeroplanes_test, altitude_range="")


@patch('builtins.input', lambda _: '1')
def test_sort_aeroplanes(aeroplanes_test):
    result = sort_aeroplanes(aeroplanes_test)
    assert result[0]["geo_altitude"] == 4091.94
    assert result[1]["geo_altitude"] == 4503.42
    assert result[2]["geo_altitude"] == 7277.1
    assert result[3]["geo_altitude"] == 11666.22


def test_get_top_aeroplanes(aeroplanes_test):
    top_n = 3
    result = get_top_aeroplanes([], top_n)
    assert len(result) == 0
    top_n = 3
    result = get_top_aeroplanes(aeroplanes_test, top_n)
    assert len(result) == top_n


@pytest.fixture
def print_result():
    return ["Hello World"]
def test_print_aeroplanes(print_result):
    sys.stdout = StringIO()
    print_aeroplanes(print_result)
    captured = sys.stdout.getvalue()
    assert  captured.strip() == str(["Hello World"])
