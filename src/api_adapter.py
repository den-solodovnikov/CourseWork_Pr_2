from abc import ABC, abstractmethod

from requests import get


class Adapter(ABC):
    @abstractmethod
    def get_coordinates(self, country):
        pass

    @abstractmethod
    def get_aeroplanes(self, country):
        pass


class APIAdapter(Adapter):
    """ Класс подключается к API и получает географические координаты стран и информацию о самолетах,
    находящихся в воздушном пространстве этих стран. """
    def __init__(self):
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.geo_coordinates = None
        self.aeroplanes = None

    def get_coordinates(self, country: str) -> None:
        """ Функция получения координат крайних точек страны, указанной в атрибутах. """
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        # Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1
        }
        try:
            response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
            if response.status_code == 200:
                data = response.json()
                self.geo_coordinates = data[0].get('boundingbox')
            else:
                print(f'Ошибка соединения. Код: {response.status_code}')
        except Exception as e:
            print(f'Ошибка: {e}\nКоординаты страны "{country}" не найдены')

    def get_aeroplanes(self, country: str) -> None:
        """ Функция получения информации о самолетах находящихся на территории указанной страны. """
        self.get_coordinates(country)
        coordinates = self.geo_coordinates
        if not coordinates:
            print('Координаты не получены')
        else:
            # Параметры для фильтрации самолетов по их географическим координатам.
            params_opensky = {
                'lamin': self.geo_coordinates[0],
                'lamax': self.geo_coordinates[1],
                'lomin': self.geo_coordinates[2],
                'lomax': self.geo_coordinates[3],
            }
            try:
                response = get(url=self.opensky_url, params=params_opensky)
                if response.status_code == 200:
                    self.aeroplanes = response.json()
                else:
                    print('Нет информации о полетах')
            except Exception as e:
                print(f'Ошибка соединения:\n{e}')
