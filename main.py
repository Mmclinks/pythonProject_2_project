from src.file_connector import JSONSaver
from src.hh_api import HeadHunterAPI
from src.user_interface import delete_vacancy, filter_data, search_query
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция взаимодействия с пользователем."""
    user_query, pages, per_pages = search_query()

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(user_query, pages, per_pages)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver("data/hh.json")
    json_saver.add_vacancies(vacancies_list)

    filter_words, salary, top_n = filter_data()

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)

    del_number = delete_vacancy()
    json_saver.delete_vacancy(del_number)


if __name__ == "__main__":
    user_interaction()
