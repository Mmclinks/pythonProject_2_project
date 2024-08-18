import json
from unittest.mock import MagicMock, patch

import pytest

from src.api import HhAPI
from src.interaction import save_vacancies_to_file
from src.interaction import (
    search_vacancies,
    get_top_n_vacancies,
    find_vacancies_by_keyword,
    user_interaction
)


# Фикстура для HhAPI
@pytest.fixture
def hh_api():
    return MagicMock(spec=HhAPI)


# Тестирование функции search_vacancies
@patch('builtins.input', side_effect=['программист', '5'])
@patch('builtins.print')
def test_search_vacancies(mock_print, mock_input, hh_api):
    # Настроим имитацию ответа API
    hh_api.get_vacancies.return_value = [
        {'name': 'Программист', 'employer': {'name': 'Компания'},
         'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'}}
    ]

    search_vacancies(hh_api)

    mock_print.assert_called_with(
        "1. Программист (Компания) - от 60000 до 80000 RUR"
    )


@patch('builtins.input', side_effect=['разработчик', '3'])
@patch('builtins.print')
def test_get_top_n_vacancies(mock_print, mock_input, hh_api):
    hh_api.get_vacancies.return_value = [
        {'name': 'Разработчик',
         'employer': {'name': 'Компания'},
         'salary': {'from': 80000,
                    'to': 100000, 'currency': 'RUR'}},
        {'name': 'Старший разработчик',
         'employer': {'name': 'Компания'},
         'salary': {'from': 90000, 'to': 120000, 'currency': 'RUR'}},
        {'name': 'Junior разработчик',
         'employer': {'name': 'Компания'},
         'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'}}
    ]

    get_top_n_vacancies(hh_api)

    # Проверяем, что правильная вакансия была выведена первой
    mock_print.assert_any_call('1. Старший разработчик (Компания) - от 90000 до 120000 RUR')
    mock_print.assert_any_call('2. Разработчик (Компания) - от 80000 до 100000 RUR')


# Тестирование функции find_vacancies_by_keyword
@patch('builtins.input', side_effect=['Python'])
@patch('builtins.print')
def test_find_vacancies_by_keyword(mock_print, mock_input, hh_api):
    hh_api.get_vacancies.return_value = [
        {'name': 'Python Developer', 'employer': {'name': 'Компания'},
         'snippet': {'responsibility': 'Знание Python', 'requirement': 'Опыт работы'}},
        {'name': 'Java Developer', 'employer': {'name': 'Компания'},
         'snippet': {'responsibility': 'Знание Java', 'requirement': 'Опыт работы'}}
    ]

    find_vacancies_by_keyword(hh_api)

    mock_print.assert_called_with(
        "1. Python Developer (Компания) - Зарплата не указана"
    )


# Тестирование функции save_vacancies_to_file




# Тестирование функции user_interaction
@patch('builtins.input', side_effect=['1', 'программист', '5', '4', 'разработчик', '3', 'Python', '5'])
@patch('builtins.print')
@patch('src.interaction.save_vacancies_to_file')
@patch('src.interaction.HhAPI')
def test_user_interaction(mock_HhAPI, mock_save_vacancies, mock_print, mock_input):
    mock_api_instance = MagicMock()
    mock_HhAPI.return_value = mock_api_instance
    mock_api_instance.get_vacancies.side_effect = [
        [{'name': 'Программист', 'employer': {'name': 'Компания'},
          'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'}}],
        [{'name': 'Разработчик', 'employer': {'name': 'Компания'},
          'salary': {'from': 80000, 'to': 100000, 'currency': 'RUR'}}],
        [{'name': 'Python Developer', 'employer': {'name': 'Компания'},
          'snippet': {'responsibility': 'Знание Python', 'requirement': 'Опыт работы'}}]
    ]

    user_interaction()

    assert mock_save_vacancies.call_count == 1
    assert mock_print.call_count > 0
