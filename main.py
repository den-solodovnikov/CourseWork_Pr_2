from pprint import pprint

from src.aeroplanes import Aeroplane
from src.api_adapter import APIAdapter
from src.config import config
from src.db_manager import DBManager, DBCreater
from src.services import (filter_aeroplanes, get_aeroplanes_by_altitude, sort_aeroplanes,
                          get_top_aeroplanes, print_aeroplanes)
from src.utils import JSONSaver



def user_interaction():
    """ Функция для взаимодействия с пользователем. """
#     country = input("Введите название страны: ")
#     top_n = int(input("Введите количество самолетов для вывода в топ N: "))
#     filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
#     altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
#
    # get_country_codes()
    # country = 'Canada'
    # api = APIAdapter()
    # api.get_aeroplanes(country)
    # aeroplane_data = api.aeroplanes

    db_params = config()
    db = DBManager(db_params)
    # db.drop_db()
    # db.create_db()
    # db.close()
    # db.create_tables()
    # db.insert_data_countries()
    # db.clear_table_aeroplanes()
    # db.insert_data_aeroplanes(['France', 'Canada'])
    # rows = db.get_countries_and_aeroplanes_count()
    # rows = db.get_all_aeroplanes()
    # rows = db.get_avg_speed()
    # rows = db.get_aeroplanes_with_higher_speed()
    rows = db.get_aeroplanes_with_keyword(['VOI3343', 'EJA914', 'AAL1390'])
    print(type(rows), rows)


#     aeroplanes = Aeroplane.cast_to_object_list(aeroplane_data)
#
#     filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
#
#     json_saver = JSONSaver('filtered_data.json')
#     json_saver.add_aeroplane(filtered_aeroplanes)
#
#     ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)
#
#     sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
#
#     top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
#     print_aeroplanes(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()
