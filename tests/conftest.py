import pytest

from src.aeroplanes import Aeroplane
from src.api_adapter import APIAdapter


@pytest.fixture
def api():
    return APIAdapter()

@pytest.fixture
def aeroplane1():
    return Aeroplane(
        code = "451cc1",
        callsign = "LZB9067",
        country_reg = "Bulgaria",
        geo_altitude = 9666.22,
        velocity = 815.05
    )


@pytest.fixture
def aeroplane2():
    return Aeroplane(
        code = "451cc2",
        callsign = "BOING767",
        country_reg = "Spain",
        geo_altitude = 6166.22,
        velocity = 615.05
    )


@pytest.fixture
def aeroplanes_data():
    return {'time': 1779386930,
            'states':[
                ['a1abea', 'N2069K', 'United States', 1779386930, 1779386930, -123.0299, 43.1088, 2697.48, False,
                 103.89, 172.03, 0, None, 2758.44, None, False, 0],
                ['a4b208', 'N401TG', 'Canada', 1779386753, 1779386756, -122.5816, 42.0033, 2247.9, False, 101.21,
                 162.85, 0.33, None, 2316.48, None, False, 0],
                ['a8dc9f', 'NCJ70', 'UK', 1779386925, 1779386925, -93.2172, 44.8775, None, True, 0,
                 84.38, None, None, None, None, False, 0]
            ]
            }


@pytest.fixture
def aeroplanes_test():
    return [
        {
            "code": "39856f",
            "callsign": "AFR74LC ",
            "country_reg": "France",
            "geo_altitude": 7277.1,
            "velocity": 216.04
        },
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
