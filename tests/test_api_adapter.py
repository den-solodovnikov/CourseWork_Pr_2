import json
from unittest.mock import patch, Mock, mock_open

from src.api_adapter import APIAdapter


def test_stock_prices_api_init():
    adapter = APIAdapter()
    assert adapter.openstreetmap_url == 'https://nominatim.openstreetmap.org/search'
    assert adapter.opensky_url == 'https://opensky-network.org/api/states/all?'


# @patch('requests.get')
# def test_get_coordinates_success(mock_get):
#     mock_response = Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = [{'boundingbox': ['50.0', '60.0', '10.0', '20.0']}]
#     mock_get.return_value = mock_response
#     adapter = APIAdapter()
#     adapter.get_coordinates('Canada')
#     assert len(adapter.geo_coordinates) == 4
#     assert adapter.geo_coordinates == ['50.0', '60.0', '10.0', '20.0']
#     assert adapter.geo_coordinates[0] == '50.0'
#     assert adapter.geo_coordinates[2] == '60.0'
#     mock_response.json.assert_called_once()
