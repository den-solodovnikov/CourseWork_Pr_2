from abc import ABC, abstractmethod
from typing import Any


class Aeroplanes(ABC):
    @abstractmethod
    def add_aeroplane(self):
        pass

    @abstractmethod
    def cast_to_object_list(self, country):
        pass


class Aeroplane(Aeroplanes):
    """ Класс для работы с информацией о самолетах. """
    code: str  # - уникальный идентификатор борта
    callsign: str  # - позывной рейса
    country_reg: str  # - страна регистрации ВС
    velocity: float  # - горизонтальная скорость(м/с)
    geo_altitude: float  # - геометрическая высота(м)
    aeroplane_list = []

    def __init__(self, code, callsign, country_reg, geo_altitude, velocity) -> None:
        self.code = code
        self.callsign = callsign
        self.country_reg = country_reg
        self.geo_altitude = geo_altitude
        self.velocity = velocity

    def add_aeroplane(self) -> None:
        pass

    @classmethod
    def cast_to_object_list(cls, aeroplanes_data: dict) -> list[Any]:
        """ Функция преобразования набора данных в список объектов класса. """
        aeroplanes_list = aeroplanes_data.get('states')
        for item in aeroplanes_list:
            new_aeroplane = cls(
                code=item[0],
                callsign=item[1],
                country_reg=item[2],
                velocity=item[9],
                geo_altitude=item[13]
            )
            cls.aeroplane_list.append(new_aeroplane.__dict__)
        return cls.aeroplane_list
