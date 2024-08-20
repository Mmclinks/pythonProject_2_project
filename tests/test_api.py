import pytest
from unittest.mock import patch, MagicMock
from src.api import HhAPI
import requests


@pytest.fixture
def hh_api():
    return HhAPI()


@patch('src.api.requests.get')
def test_get_vacancies_success(mock_get, hh_api):
    # Настроим имитацию ответа API
    mock_get.return_value.json.return_value = {
        'items': [
            {'name': 'Программист', 'employer': {'name': 'Компания'},
             'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'}}
        ]
    }

    # Вызовем метод get_vacancies и проверим его результат
    vacancies = hh_api.get_vacancies(text='программист')
    assert len(vacancies) == 1
    assert vacancies[0]['name'] == 'Программист'


@patch('src.api.requests.get')
def test_get_vacancies_failure(mock_get, hh_api):
    # Настроим имитацию ошибки HTTP
    mock_get.side_effect = requests.exceptions.HTTPError('Ошибка HTTP')

    # Проверим, что get_vacancies корректно обрабатывает исключение
    with pytest.raises(requests.exceptions.HTTPError):
        hh_api.get_vacancies(text='программист')


@patch('src.api.requests.get')
def test_make_request_success(mock_get, hh_api):
    # Настроим имитацию успешного ответа API
    mock_get.return_value.json.return_value = {
        'items': [
            {'name': 'Аналитик', 'employer': {'name': 'Аналитика'},
             'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'}}
        ]
    }

    # Вызовем приватный метод _make_request и проверим его результат
    response = hh_api._make_request('vacancies', {'text': 'аналитик'})
    assert 'items' in response
    assert len(response['items']) == 1
    assert response['items'][0]['name'] == 'Аналитик'


@patch('src.api.requests.get')
def test_make_request_failure(mock_get, hh_api):
    # Настроим имитацию ошибки HTTP
    mock_get.side_effect = requests.exceptions.RequestException('Ошибка запроса')

    # Проверим, что _make_request корректно обрабатывает исключение
    with pytest.raises(requests.exceptions.RequestException):
        hh_api._make_request('vacancies', {'text': 'аналитик'})
