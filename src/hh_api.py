from typing import List, Optional

import requests

from src.api_connector import ApiParser


class HeadHunterAPI(ApiParser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self) -> None:
        """Инициализатор класса. Все атрибуты приватные."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 2, "per_page": 5}
        self.__vacancies: List = []

    def _get_response(
        self, keyword: str, pages: int, per_page: int
    ) -> Optional[requests.Response]:
        """Метод подключения к API"""
        self.__params["text"] = keyword
        self.__params["page"] = pages
        self.__params["per_page"] = per_page

        try:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )

            if response.status_code == 200:
                return response
            else:
                raise Exception(
                    f"Failed to connect to API. Status code: {response.status_code}"
                )
        except Exception as e:
            print(f"Непредвиденная ошибка - {e}")

    def get_vacancies(self, keyword: str, pages: int, per_page: int) -> List:
        """Метод преобразования ответа с API в объект"""
        all_vacancies = []
        for page in range(pages):
            response = self._get_response(keyword, page, per_page)
            if response:
                vacancies = response.json().get("items", [])
                all_vacancies.extend(vacancies)
        return all_vacancies
