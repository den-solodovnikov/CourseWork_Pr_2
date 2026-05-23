# Курсовая работа. 
# Проект 2. "Трекер самолётов"


## Описание:

Проект "Трекер самолётов" - это приложение на Python, 
которое собирает данные о самолетах в воздушных пространствах 
выбранной пользователем страны.


## Установка:

+ Установите на свой компьютер GitHub.
+ Клонируйте репозиторий с GitHub с помощью веб-URL.
```
 git clone git@github.com:den-solodovnikov/CourseWork_Pr_2.git
```


## Использование:

В текущем виде, программа запускается в модуле main.py:
Для проверки работы функций в модуле main.py

## Структура проекта:
.
├── src
│ ├── __init__.py
│ ├── aeroplanes.py
│ ├── api_adapder.py
│ ├── utils.py
│ └── services.py
├── data
│ ├── data_aeroplane.json
├── tests
│ ├── __init__.py
│ ├── test_aeroplanes.py
│ ├── test_api_adapter.py
│ ├── test_utils.py
│ └── test_services.py
├── main.py
├── .venv/
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md


## Примеры использования функций:

+ Модуль aeroplanes описывает класс Aeroplane и содержит методы этого класса:

**class Aeroplane(Aeroplanes):**
Класс для работы с информацией о самолетах.

**def cast_to_object_list(cls, aeroplanes_data) -> list[Any]:**
Функция преобразования набора данных в список объектов класса.

+ Модуль api_adapter содержит класс сбора данных о самолетах в определенном географическом пространстве:

**class APIAdapter(Adapter):**
Класс подключается к API и получает географические координаты стран и информацию о самолетах,
находящихся в воздушном пространстве этих стран.

**def get_coordinates(self, country: str) -> None:**
Функция обращается к внешнему API (https://nominatim.openstreetmap.org/) 
для получения координат крайних точек страны, указанной в атрибутах.

**def get_aeroplanes(self, country: str) -> None:**
Функция получения информации о самолетах находящихся на территории указанной страны из внешнего API-источника
(https://opensky-network.org).


+ Модуль services содержит сервисные функции для отбора и сортировки данных:

**def filter_aeroplanes(aeroplanes: list, filter_words: list[str]) -> list**
Функция возвращает список самолетов, зарегистрированных в указанных странах.

**def get_aeroplanes_by_altitude(aeroplanes: list, altitude_range: str) -> list:**
Функция возвращает список самолетов с высотой полета, указанном в диапазоне высот (Пример: 1000 - 5000).

**def sort_aeroplanes(ranged_aeroplanes: list) -> list:**
Функция возвращает отсортированный список самолетов по высоте или скорости.

**def get_top_aeroplanes(sorted_aeroplanes, top_n) -> list:**
Функция возвращает топ-N отсортированных самолетов.

**def print_aeroplanes(top_aeroplanes: list) -> None:**
Функция вывода в консоль.

+ Модуль utils содержит класс для чтения и записи данных в файлы:

**class JSONSaver(Saver):**
Класс для добавления и изменения информации о самолете в JSON-файл.

**def add_aeroplane(self, vacancy: dict | list) -> None:**
Функция добавления информации о самолете в файл.

**def load_aeroplane(self, params: list[str]) -> list | None:**
Функция получения данных из файла по указанным критериям.

**def delete_aeroplane(self, vacancy: str) -> None:**
Функция удаления информации о самолетах.


## Разработка:

+ Проект находится в активной разработке. План работы в дальнейшем:

+ Добавление новых модулей для расширения функционала

+ Улучшение обработки различных форматов данных

+ Добавление тестов

+ Выполнение всех ТЗ курсовой работы 


## Автор проекта:

 Denis Solodovnikov