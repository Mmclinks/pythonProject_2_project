from abc import ABC, abstractmethod
from typing import List, Optional
from unittest.mock import MagicMock

import requests


class ApiParser(ABC):
    @abstractmethod
    def _get_response(self, keyword: str, page: int, per_page: int) -> Optional[requests.Response]:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, page: int, per_page: int) -> List:
        pass


class Files(ABC):
    @abstractmethod
    def get_data(self) -> List:
        pass

    @abstractmethod
    def add_vacancies(self, hh_vacancies: List) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, del_number: str) -> List | None:
        pass


# Тестовые реализации абстрактных классов для тестирования
class TestApiParser(ApiParser):
    def _get_response(self, keyword: str, page: int, per_page: int) -> Optional[requests.Response]:
        # Простая заглушка для тестов
        response = MagicMock()
        response.json.return_value = {"items": []}
        return response

    def get_vacancies(self, keyword: str, page: int, per_page: int) -> List:
        return self._get_response(keyword, page, per_page).json()["items"]


class TestFiles(Files):
    def __init__(self):
        self.data = []

    def get_data(self) -> List:
        return self.data

    def add_vacancies(self, hh_vacancies: List) -> None:
        self.data.extend(hh_vacancies)

    def delete_vacancy(self, del_number: str) -> List | None:
        self.data = [v for v in self.data if v["id"] != del_number]
        return self.data


# Тесты с использованием pytest
def test_get_response():
    api_parser = TestApiParser()
    response = api_parser._get_response("python", 1, 10)
    assert response is not None
    assert response.json() == {"items": []}


def test_get_vacancies():
    api_parser = TestApiParser()
    vacancies = api_parser.get_vacancies("python", 1, 10)
    assert isinstance(vacancies, list)
    assert len(vacancies) == 0


def test_get_data():
    files = TestFiles()
    data = files.get_data()
    assert isinstance(data, list)
    assert len(data) == 0


def test_add_vacancies():
    files = TestFiles()
    new_vacancies = [{"id": "1", "title": "Python Developer"}]
    files.add_vacancies(new_vacancies)
    assert len(files.get_data()) == 1
    assert files.get_data()[0]["id"] == "1"


def test_delete_vacancy():
    files = TestFiles()
    files.add_vacancies([{"id": "1", "title": "Python Developer"}])
    files.delete_vacancy("1")
    assert len(files.get_data()) == 0
