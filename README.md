# HeadHunter

Программа, которая будет получать информацию о вакансиях с платформы hh.ru в России, сохранять ее в файл и
позволять удобно работать с ней: добавлять, фильтровать, удалять.

## Структура проекта

├── src
│ ├── api.py
│ ├── interaction.py
│ ├── utils.py
│ ├── main.py
├── tests
│ ├── test_api.py
│ ├── test_interaction.py
│ ├── test_utils.py
│ ├── test_main.py


### Модули

- **api.py**: Модуль, содержащий абстрактный класс для работы с API сервиса с вакансиями.
- **interaction.py**: Модуль содержит функцию для взаимодействия с пользователем.
- **utils.py**: Модуль для обработки информации о зарплате.
- **main.py**: Точка входа.

## Установка

1. Клонируйте репозиторий:

git clone https://github.com/Mmclinks/pythonProject_2_project.git

   
2. Установите зависимости:
pip install
или
poetry install


- Тестирование

Запустите тесты с помощью pytest:

pytest

Покрытие кода:


F---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
src/__init__.py                 0      0   100%
src/api.py                     24      2    92%
src/interaction.py             66      8    88%
src/utils.py                    5      0   100%
tests/__init__.py               0      0   100%
tests/test_api.py              30      0   100%
tests/test_interaction.py      39      0   100%
tests/test_utils.py            22      0   100%
-----------------------------------------------
TOTAL                         186     10    95%

Лицензия:

Этот проект лицензирован по лицензии[MIT].

Этот README.md файл предоставляет информацию о проекте, его 
структуре, установке, использовании, тестировании и лицензии.
