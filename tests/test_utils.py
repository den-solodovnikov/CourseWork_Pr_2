import unittest
from unittest.mock import patch

import pytest

from src.utils import JSONSaver


# @patch('json.load')
# @patch('builtins.open', new_callable=unittest.mock.mock_open)
# def test_read_json_success(mock_open, mock_load):
#     saver = JSONSaver()
#     mock_load.return_value = {
#         'code': '451cc1',
#         'callsign': 'LZB9067',
#         'country_reg': 'Bulgaria',
#         'geo_altitude': 9666.22,
#         'velocity': 815.05
#     }
#     assert saver.add_aeroplane(aeroplane1) == {
#         'code': '451cc1',
#         'callsign': 'LZB9067',
#         'country_reg': 'Bulgaria',
#         'geo_altitude': 9666.22,
#         'velocity': 815.05
#     }
#     mock_open.assert_called_once_with('D:\\PYTHON\\data\\products.json', 'r', encoding="utf-8")

def test_read_json_error():
    # Тестируем поведение при ошибке (например, файл не найден)
    with pytest.raises(FileNotFoundError) as excinfo:
        open("bad_path.json")
    assert "bad_path.json" in str(excinfo.value)
