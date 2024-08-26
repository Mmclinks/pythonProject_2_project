import pytest

from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies
from src.vacancy import Vacancy


# Фикстура для создания списка вакансий
@pytest.fixture
def vacancies_list():
    return [
        Vacancy("1", "Python Developer", "https://example.com/1", "Python, Django", 120000),
        Vacancy("2", "Java Developer", "https://example.com/2", "Java, Spring", 110000),
        Vacancy("3", "Data Scientist", "https://example.com/3", "Python, Machine Learning", 130000),
        Vacancy("4", "DevOps Engineer", "https://example.com/4", "Docker, Kubernetes", 125000),
        Vacancy("5", "Frontend Developer", "https://example.com/5", "JavaScript, React", 115000),
    ]


# Тесты для функции filter_vacancies

def test_filter_vacancies(vacancies_list):
    filtered = filter_vacancies(vacancies_list, "Python")
    assert len(filtered) == 2
    assert filtered[0].name == "Python Developer"
    assert filtered[1].name == "Data Scientist"


def test_filter_vacancies_no_match(vacancies_list):
    filtered = filter_vacancies(vacancies_list, "Ruby")
    assert len(filtered) == 0


# Тесты для функции get_vacancies_by_salary

def test_get_vacancies_by_salary(vacancies_list):
    filtered = filter_vacancies(vacancies_list, "Python")
    ranged = get_vacancies_by_salary(filtered, 125000)
    assert len(ranged) == 1
    assert ranged[0].name == "Data Scientist"


def test_get_vacancies_by_salary_no_match(vacancies_list):
    filtered = filter_vacancies(vacancies_list, "Python")
    ranged = get_vacancies_by_salary(filtered, 150000)
    assert len(ranged) == 0


# Тесты для функции sort_vacancies

def test_sort_vacancies(vacancies_list):
    sorted_vacancies = sort_vacancies(vacancies_list)
    assert sorted_vacancies[0].salary == 110000
    assert sorted_vacancies[-1].salary == 130000


# Тесты для функции get_top_vacancies

def test_get_top_vacancies(vacancies_list):
    sorted_vacancies = sort_vacancies(vacancies_list)
    top_vacancies = get_top_vacancies(sorted_vacancies, 3)
    assert len(top_vacancies) == 3
    assert top_vacancies[0].salary == 110000
    assert top_vacancies[-1].salary == 120000


def test_get_top_vacancies_more_than_available(vacancies_list):
    sorted_vacancies = sort_vacancies(vacancies_list)
    top_vacancies = get_top_vacancies(sorted_vacancies, 10)
    assert len(top_vacancies) == len(sorted_vacancies)


# Тест для функции print_vacancies

def test_print_vacancies(capsys, vacancies_list):
    top_vacancies = get_top_vacancies(vacancies_list, 2)
    print_vacancies(top_vacancies)
    captured = capsys.readouterr()
    assert "Python Developer" in captured.out
    assert "Java Developer" in captured.out
