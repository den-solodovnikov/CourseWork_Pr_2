from pprint import pprint

import psycopg2
import pycountry
from psycopg2.extras import DictCursor, DictRow

from src.aeroplanes import Aeroplane
from src.api_adapter import APIAdapter
from tests.conftest import aeroplane1

class DB:
    def __init__(self, db_params: dict, db_name: str = 'db_aeroplanes'):
        self.db_name = db_name
        self.conn = psycopg2.connect(**db_params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()


class DBCreater(DB):
    """ Класс для создания и удаления базы данных PostgreSQL. """
    def __init__(self, db_params: dict, db_name: str = 'db_aeroplanes'):
        super().__init__(db_params, db_name)

    def drop_db(self):
        """ Функция удаления базы данных. """
        try:
            self.cur.execute(f"DROP DATABASE {self.db_name} WITH (FORCE);")
        except psycopg2.Error as e:
            print(f'Ошибка удаления БД "{self.db_name}": {e}')
        self.cur.close()

    def create_db(self):
        """ Функция создания базы данных. """
        # self.cur = self.conn.cursor()
        try:
            self.cur.execute(f'CREATE DATABASE {self.db_name};')
            # self.conn.commit()
        except psycopg2.Error as e:
            print(f'Ошибка создания БД "{self.db_name}": {e}')
        self.cur.close()



class DBManager(DB):
    """ Класс для работы с данными в БД PostgreSQL. """
    def __init__(self, db_params: dict, db_name: str = 'db_aeroplanes'):
        super().__init__(db_params, db_name)
        self.conn = psycopg2.connect(dbname=self.db_name, **db_params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor(cursor_factory=DictCursor)

    def create_tables(self):
        """ Функция создания таблиц 'countries' и 'aeroplanes' в БД. """
        # self.cur = self.conn.cursor()
        try:
            self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS countries 
                            (
                                numeric VARCHAR(3) PRIMARY KEY NOT NULL,
                                ISO2 VARCHAR(2) NOT NULL,
                                ISO3 VARCHAR(3) NOT NULL,
                                name VARCHAR(100) NOT NULL
                            );
                        CREATE TABLE IF NOT EXISTS aeroplanes 
                            (
                                airs_id SERIAL PRIMARY KEY NOT NULL,
                                code VARCHAR(50),
                                callsign VARCHAR(50),
                                country_reg VARCHAR(100),
                                geo_altitude real,
                                velocity real,
                                numeric VARCHAR(3) REFERENCES countries("numeric") NOT NULL
                            );
                            """)
            # self.conn.commit()

        except psycopg2.Error as e:
            print(f'Ошибка создания таблиц "{self.db_name}": {e}')
        # self.close()

    def clear_table_aeroplanes(self):
        """ Функция очищает таблицу 'aeroplanes'. """
        try:
            self.cur.execute("TRUNCATE TABLE aeroplanes;")
        except psycopg2.Error as e:
            print(f'Ошибка удаления данных из таблицы "aeroplanes": {e}')


    def insert_data_countries(self):
        """ Функция заполняет таблицу 'countries' данными (выбирает список всех стран мира). """
        for country in pycountry.countries:
            self.cur.execute("INSERT INTO countries (numeric, iso2, iso3, name) VALUES (%s, %s, %s, %s)",
                             (country.numeric, country.alpha_2, country.alpha_3, country.name)
                             )

    def insert_data_aeroplanes(self, params: list[str]):
        """ Функция заполняет таблицу 'aeroplanes' данными. """
        self.cur = self.conn.cursor()
        countries = []
        try:
            self.cur.execute(f"SELECT DISTINCT * FROM countries "
                             f"WHERE name IN ({str(params).replace('[', '').replace(']','')}) "
                             f"ORDER BY name;")
            rows = self.cur.fetchall()
            for row in rows:
                countries.append({f'{str(row[0]).strip()}': f'{str(row[3]).strip()}'})
        except psycopg2.Error as e:
            print(f'Ошибка чтения таблицы "countries": {e}')
        api = APIAdapter()
        for i in range(len(countries)):
            for key, value in countries[i].items():
                aeroplanes = []
                api.get_aeroplanes(value)
                aeroplanes = api.aeroplanes
                print(i, ' -- ', value)
                # print(aeroplanes)
                if aeroplanes:
                    # print(value)
                    data_aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
                    # print(type(data_aeroplanes), data_aeroplanes)
                    for data in data_aeroplanes:
                        self.cur.execute("""INSERT INTO aeroplanes (code, callsign, country_reg, geo_altitude, velocity, numeric)
                                        VALUES (%s, %s, %s, %s, %s, %s)
                                     """,
                                     (
                                         data.get('code'), data.get('callsign'), data.get('country_reg'),
                                         data.get('geo_altitude'), data.get('velocity'), key
                                     )
                                     )

    def close(self):
        self.cur = self.conn.cursor()
        self.cur.close()
        self.conn.close()

    def get_countries_and_aeroplanes_count(self) -> list[DictRow] | None:
        """ Возвращает список всех стран и количество самолетов в их воздушных пространствах. """
        try:
            self.cur.execute("SELECT countries.name, COUNT (*) FROM countries "
                             "INNER JOIN aeroplanes USING (numeric) "
                             "GROUP BY countries.name;")
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def get_all_aeroplanes(self) -> list[DictRow] | None:
        """ Возвращает список всех воздушных судов. """
        try:
            self.cur.execute("SELECT DISTINCT * FROM aeroplanes "
                             "ORDER BY airs_id;")
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def get_avg_speed(self) -> list[DictRow] | None:
        """ Возвращает среднюю скорость по самолетам. """
        try:
            self.cur.execute("SELECT AVG (velocity) FROM aeroplanes;")
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def get_aeroplanes_with_higher_speed(self) -> list[DictRow] | None:
        """ Возвращает список всех самолетов, у которых скорость выше средней. """
        try:
            self.cur.execute("SELECT * FROM aeroplanes "
                             "WHERE velocity > (SELECT AVG (velocity) FROM aeroplanes);")
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def get_aeroplanes_with_keyword(self, params: list[str]) -> list[DictRow] | None:
        """ Возвращает список всех самолетов, в позывном которых содержатся переданные в метод символы. """
        try:
            self.cur.execute(f"SELECT DISTINCT * FROM aeroplanes "
                             f"WHERE callsign IN ({str(params).replace('[', '').replace(']', '')}) "
                             f"ORDER BY callsign;")
            return self.cur.fetchall()
        except Exception as e:
            print(e)
