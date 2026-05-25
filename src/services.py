import re
from pprint import pprint


def filter_aeroplanes(aeroplanes: list, filter_words: list[str]) -> list:
    """ Функция возвращает список самолетов, зарегистрированных в указанных странах. """
    data_filtered = []
    for aeroplane in aeroplanes:
        for word in filter_words:
            if word in aeroplane.get('country_reg'):
                data_filtered.append(aeroplane)
    return data_filtered


def get_aeroplanes_by_altitude(aeroplanes: list, altitude_range: str) -> list:
    """ Функция возвращает список самолетов с высотой полета, указанном в диапазоне высот (Пример: 1000 - 5000). """
    numbers = re.findall(r'-?\d+', altitude_range)
    data_filtered = []
    try:
        altitude_lower, altitude_high = float(numbers[0]), float(numbers[1])
    except IndexError as e:
        print('Не переданы параметры высот')
        altitude_lower, altitude_high = 0, 0
    for aeroplane in aeroplanes:
        if (isinstance(aeroplane.get('geo_altitude'), float) and
                altitude_lower <= float(aeroplane.get('geo_altitude')) <= altitude_high):
            data_filtered.append(aeroplane)
    return data_filtered


def sort_aeroplanes(ranged_aeroplanes: list) -> list:
    """ Функция возвращает отсортированный список самолетов по высоте или скорости. """
    key_ = input('Сортировка по высоте полета, введите - 1\n'
                 'Сортировка по скорости полета, введите - 2\n')
    key_sort = 'geo_altitude'
    if key_ == '2':
        key_sort = 'velocity'
    elif key_ != '1':
        print('Не выбран параметр сортировки. По умолчанию список будет отсортирован по высоте полета')
    aeroplanes_sorted = sorted(ranged_aeroplanes, key=lambda x: x.get(key_sort))
    return aeroplanes_sorted


def get_top_aeroplanes(sorted_aeroplanes, top_n) -> list:
    """ Функция возвращает топ-N отсортированных самолетов. """
    if top_n > len(sorted_aeroplanes):
        top_n = len(sorted_aeroplanes)
    return sorted_aeroplanes[:top_n]


def print_aeroplanes(top_aeroplanes: list) -> None:
    """ Функция вывода в консоль. """
    pprint(top_aeroplanes)
