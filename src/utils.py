import json
import iso3166
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def add_aeroplane(self, data):
        pass

    @abstractmethod
    def load_aeroplane(self, data):
        pass

    @abstractmethod
    def delete_aeroplane(self, data):
        pass


class JSONSaver(Saver):
    """ Класс для добавления и изменения информации о самолете в JSON-файл. """
    file_name: str

    def __init__(self, file_name='data_aeroplane.json'):
        self.file_name = os.path.join(os.getcwd(), 'data', file_name)

    def add_aeroplane(self, vacancy: dict | list) -> None:
        """ Функция добавления информации о самолете в файл. """
        data = []
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            print(f'Файл не найден: {e}\n'
                  f'Создан файл: {self.file_name}')
        except json.decoder.JSONDecodeError as e:
            print(f'Файл пустой или не верный формат: {e}')
        if isinstance(vacancy, list):
            data.extend(vacancy)
        elif isinstance(vacancy, dict):
            data.append(vacancy)
        try:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Ошибка чтения записи\n{e}')

    def load_aeroplane(self, params: list[str]) -> list | None:
        """ Функция получения данных из файла по указанным критериям. """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f'Не удалось открыть файл:\n{e}')
        data_list = []
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                for param in params:
                    if param in item.values():
                        data_list.append(item)
        else:
            print('Не верный формат данных в файле')
        return data_list

    def delete_aeroplane(self, vacancy: str) -> None:
        """ Функция удаления информации о самолетах. """
        flag_is = False
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    for item in data:
                        if isinstance(item, dict):
                            if vacancy in item.values():
                                flag_is = True
                                print(f'Будет удалена запись о судне с параметром: {vacancy}')
                                confirm = input('Продолжить удаление? (yes/no):\n')
                                if confirm.lower() == 'yes':
                                    data.remove(item)
                                    print('Запись успешно удалена')
                else:
                    print('Записи в файле отсутствуют или не соответствуют формату JSON')
        except Exception as e:
            print(f'Ошибка записи данных в файл:\n{e}')

        try:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                if not flag_is:
                    print(f'Запись с данными {vacancy} не найдена')

        except Exception as e:
            print(f'Ошибка записи в файл:\n{e}')
