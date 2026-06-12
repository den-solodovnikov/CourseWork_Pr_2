import json
from unittest.mock import patch, Mock, mock_open

from src.api_adapter import APIAdapter


def test_stock_prices_api_init():
    adapter = APIAdapter()
    assert adapter.openstreetmap_url == 'https://nominatim.openstreetmap.org/search'
    assert adapter.opensky_url == 'https://opensky-network.org/api/states/all?'


# @patch('APIAdapter.get_coordinates')
# def test_get_coordinates_success():
#     # mock_response = Mock()
#     with patch('src.api_adapter.APIAdapter.get_coordinates') as mock_get:
#         mock_get.status_code = 200
#         mock_get.return_value = {}
#         # mock_get.return_value = mock_response
#     adapter = APIAdapter()
#     # adapter.get_coordinates('Canada')
#     assert type(adapter.geo_coordinates()) == dict
#     # assert adapter.geo_coordinates == ['50.0', '60.0', '10.0', '20.0']
#     # assert adapter.geo_coordinates[0] == '50.0'
#     # assert adapter.geo_coordinates[2] == '60.0'
#     # mock_response.json.assert_called_once()
