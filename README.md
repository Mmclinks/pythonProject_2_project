# VacancyFinder

Программа, которая будет получать информацию о вакансиях с платформы hh.ru в России, сохранять ее в файл и
позволять удобно работать с ней: добавлять, фильтровать, удалять.

## Структура проекта

├── src
│ ├── api_connector.py
│ ├── file_connector.py
│ ├── hh_api.py
│ ├── user_interface.py
│ ├── utils.py
│ ├── vacancy.py
├── tests
│ ├── test_api_connector.py
│ ├── test_file_connector.py
│ ├── hh_api.py
│ ├── user_interface.py
│ ├── test_utils.py
│ ├── test_vacancy.py
├── main.py

### Модули

- **api_connector.py**: Модуль для работы с API и файлами.
- **file_connector.py**: Модуль для работы с файлами в формате JSON и CSV.
- **hh_api.py**: Модуль для работы с API HeadHunter.
- **user_interface.py**: Модуль для взаимодействия с пользователем.
- **utils.py**: Модуль для фильтрации и сортировки вакансий.
- **vacancy.py**: Модуль для работы с вакансиями.
- **main.py**: Точка входа.
- 
## Установка

Клонируйте репозиторий:

git clone https://github.com/Mmclinks/pythonProject_2_project.git

   
Установите зависимости:

pip install
или
poetry install


- Тестирование

Запустите тесты с помощью pytest:

pytest

Покрытие кода:


---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/__init__.py                    0      0   100%
src/api_connector.py              20      5    75%
src/file_connector.py             56     18    68%
src/hh_api.py                     28      0   100%
src/user_interface.py             34      0   100%
src/utils.py                      22      0   100%
src/vacancy.py                    80      8    90%
tests/__init__.py                  0      0   100%
tests/test_api_connector.py       64      5    92%
tests/test_file_connector.py      30      0   100%
tests/test_hh_api.py              41      0   100%
tests/test_user_interface.py      39      0   100%
tests/test_utils.py               43      0   100%
tests/test_vacancy.py             51      0   100%
--------------------------------------------------
TOTAL                            508     36    93%


Лицензия:

Этот проект лицензирован по лицензии[MIT].

Этот README.md файл предоставляет информацию о проекте, его 
структуре, установке, использовании, тестировании и лицензии.
