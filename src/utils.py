from typing import List


def filter_vacancies(vacancies_list: List, filter_words: str) -> List:
    """Функция фильтрации вакансий по ключевому слову"""
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if filter_words in vacancy.description:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: List, salary: int) -> List:
    """Функция фильтрации вакансий по зарплате"""
    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        if vacancy.salary > salary:
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def sort_vacancies(ranged_vacancies: List) -> List:
    """Функция сортировки вакансий по зарплате"""
    return sorted(ranged_vacancies, key=lambda x: x.salary)


def get_top_vacancies(sorted_vacancies: List, top_n: int = 10) -> List:
    """Функция получения первых N вакансий из списка"""
    if top_n > len(sorted_vacancies):
        top_n = len(sorted_vacancies)

    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies: List) -> None:
    """Функция вывода конечного результата в консоль"""
    for vacancy in top_vacancies:
        print(vacancy)
