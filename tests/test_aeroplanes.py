from src.aeroplanes import Aeroplane


def test_aeroplane_init(aeroplane1) -> None:
    assert aeroplane1.code == "451cc1"
    assert aeroplane1.callsign == "LZB9067"
    assert aeroplane1.country_reg == "Bulgaria"
    assert aeroplane1.geo_altitude == 9666.22
    assert aeroplane1.velocity == 815.05


def test_cast_to_object_list(aeroplanes_data):
    result = Aeroplane.cast_to_object_list(aeroplanes_data)
    assert isinstance(result, list)
    assert len(result) == 3
    assert result[0]['callsign'] == "N2069K"
    assert result[1]['country_reg'] == "Canada"
    assert result[1]['geo_altitude'] == 2316.48
    assert result[2]['velocity'] == 0
