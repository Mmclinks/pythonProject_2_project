from unittest.mock import patch

import requests

from src.hh_api import HeadHunterAPI  # Импортируйте класс из вашего модуля


# Тестируем метод _get_response
def test_get_response_success():
    api = HeadHunterAPI()

    with patch('src.hh_api.requests.get') as mock_get:
        # Настраиваем мок
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'{"items": []}'
        mock_get.return_value = mock_response

        response = api._get_response('developer', 1, 5)
        assert response.status_code == 200
        assert response.json() == {"items": []}


def test_get_response_failure():
    api = HeadHunterAPI()

    with patch('src.hh_api.requests.get') as mock_get:
        # Настраиваем мок
        mock_response = requests.Response()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        response = api._get_response('developer', 1, 5)
        assert response is None


# Тестируем метод get_vacancies
def test_get_vacancies():
    api = HeadHunterAPI()

    with patch('src.hh_api.requests.get') as mock_get:
        # Настраиваем мок для первой страницы
        mock_response_page_1 = requests.Response()
        mock_response_page_1.status_code = 200
        mock_response_page_1._content = b'{"items": [{"id": "1", "name": "Dev"}]}'

        # Настраиваем мок для второй страницы
        mock_response_page_2 = requests.Response()
        mock_response_page_2.status_code = 200
        mock_response_page_2._content = b'{"items": [{"id": "2", "name": "Dev2"}]}'

        mock_get.side_effect = [mock_response_page_1, mock_response_page_2]

        vacancies = api.get_vacancies('developer', 2, 5)

        assert len(vacancies) == 2
        assert vacancies[0]['id'] == '1'
        assert vacancies[1]['id'] == '2'


# Тестируем обработку исключений
def test_get_vacancies_with_exception():
    api = HeadHunterAPI()

    with patch('src.hh_api.requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        vacancies = api.get_vacancies('developer', 2, 5)

        assert vacancies == []