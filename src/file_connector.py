import csv
import json
import os
from typing import Any, List

from src.api_connector import Files


class JSONSaver(Files):
    """Класс для работы с файлами"""

    def __init__(self, file_path: str = "data/hh.json") -> None:
        self.__file_path = file_path

    def get_data(self) -> Any:
        """Получения данных из файла"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r+", encoding="utf-8") as f:
                try:
                    existing_vacancies = json.load(f)
                    return existing_vacancies

                except json.JSONDecodeError:
                    existing_vacancies = []
                    return existing_vacancies
        else:
            existing_vacancies = []
            return existing_vacancies

    def add_vacancies(self, vacancies_list: List) -> None:
        """Добавления вакансий в файл"""
        existing_vacancies = self.get_data()

        existing_vacancies_dict = {
            vacancy["id"]: vacancy for vacancy in existing_vacancies
        }

        for vacancy in vacancies_list:
            if vacancy.id_vacancy in existing_vacancies_dict:
                continue
            existing_vacancies.append(
                {
                    "id": vacancy.id_vacancy,
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "description": vacancy.description,
                    "salary": vacancy.salary,
                }
            )

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(existing_vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, del_num: int) -> Any:
        """Удаления вакансий из файла"""
        existing_vacancies = self.get_data()
        if not existing_vacancies:
            return []

        for index, vacancy in enumerate(existing_vacancies):
            if str(del_num) in vacancy.values():
                existing_vacancies.pop(index)
                with open(self.__file_path, "w", encoding="utf-8") as file:
                    json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)

                break


class CSVSaver(Files):
    """Класс для работы с CSV файлами"""

    def __init__(self, file_path: str = "data/vacancies.csv") -> None:
        """Инициализация класса"""
        self.__file_path = file_path

    def get_data(self) -> List:
        """Получения данных из CSV файла"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        return []

    def add_vacancies(self, vacancies_list: List) -> None:
        """Добавления вакансий в CSV файл"""
        with open(self.__file_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=vacancies_list[0].keys())
            if f.tell() == 0:
                writer.writeheader()
            for vacancy in vacancies_list:
                writer.writerow(vacancy)

    def delete_vacancy(self, del_number: str) -> None:
        """Удаления вакансий из CSV файла"""
        pass
