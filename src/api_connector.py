from abc import ABC, abstractmethod
from typing import List, Optional

import requests


class ApiParser(ABC):
    """Абстрактный класс для работы с API HH.RU"""

    @abstractmethod
    def _get_response(
        self, keyword: str, page: int, per_page: int
    ) -> Optional[requests.Response]:
        """Абстрактный метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, page: int, per_page: int) -> List:
        """Абстрактный метод для преобразования ответа с API в Python объект"""
        pass


class Files(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_data(self) -> List:
        """Абстрактный метод для получения данных из файла"""
        pass

    @abstractmethod
    def add_vacancies(self, hh_vacancies: List) -> None:
        """Абстрактный метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, del_number: str) -> List | None:
        """Абстрактный метод для удаления вакансий из файла"""
        pass
