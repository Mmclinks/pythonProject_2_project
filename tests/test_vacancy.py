import pytest

from src.vacancy import Vacancy

# Тесты для метода __init__ и валидаторов

def test_vacancy_init_valid():
    vacancy = Vacancy(id_vacancy="123", name="Python Developer", url="http://example.com", description="Some description", salary=100000)
    assert vacancy.id_vacancy == "123"
    assert vacancy.name == "Python Developer"
    assert vacancy.url == "http://example.com"
    assert vacancy.description == "Some description"
    assert vacancy.salary == 100000

def test_vacancy_init_invalid_id():
    with pytest.raises(ValueError, match="Invalid id"):
        Vacancy(id_vacancy="abc", name="Python Developer", url="http://example.com", description="Some description", salary=100000)

def test_vacancy_init_invalid_name():
    with pytest.raises(ValueError, match="Invalid name"):
        Vacancy(id_vacancy="123", name="", url="http://example.com", description="Some description", salary=100000)

def test_vacancy_init_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        Vacancy(id_vacancy="123", name="Python Developer", url="example.com", description="Some description", salary=100000)

def test_vacancy_init_invalid_salary():
    with pytest.raises(ValueError, match="Invalid salary_min"):
        Vacancy(id_vacancy="123", name="Python Developer", url="http://example.com", description="Some description", salary=-100)

# Тесты для методов сравнения

def test_vacancy_comparison():
    vacancy1 = Vacancy(id_vacancy="123", name="Python Developer", url="http://example.com", description="Some description", salary=100000)
    vacancy2 = Vacancy(id_vacancy="124", name="Java Developer", url="http://example.com", description="Some description", salary=120000)
    vacancy3 = Vacancy(id_vacancy="125", name="C++ Developer", url="http://example.com", description="Some description", salary=100000)

    assert vacancy1 < vacancy2
    assert vacancy2 > vacancy1
    assert vacancy1 == vacancy3
    assert vacancy1 <= vacancy3
    assert vacancy2 >= vacancy1

# Тесты для метода cast_to_object_list

def test_cast_to_object_list_valid():
    hh_vacancies = [
        {
            "id": "123",
            "name": "Python Developer",
            "alternate_url": "http://example.com",
            "snippet": {"requirement": "Some description"},
            "salary": {"from": 90000, "to": 110000}
        },
        {
            "id": "124",
            "name": "Java Developer",
            "alternate_url": "http://example.com",
            "snippet": {"requirement": "Some description"},
            "salary": {"from": 100000, "to": 120000}
        }
    ]

    vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    assert len(vacancies) == 2
    assert vacancies[0].id_vacancy == "123"
    assert vacancies[0].salary == 100000
    assert vacancies[1].id_vacancy == "124"
    assert vacancies[1].salary == 110000

def test_cast_to_object_list_invalid():
    hh_vacancies = [
        {
            "id": "abc",  # Invalid ID
            "name": "Python Developer",
            "alternate_url": "http://example.com",
            "snippet": {"requirement": "Some description"},
            "salary": {"from": 90000, "to": 110000}
        }
    ]

    vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    assert len(vacancies) == 0  # Invalid vacancy should be skipped

# Тесты для метода salary_data

def test_salary_data():
    vacancy_data = {
        "salary": {"from": 50000, "to": 70000}
    }
    assert Vacancy.salary_data(vacancy_data) == 60000

    vacancy_data = {
        "salary": {"from": 50000, "to": None}
    }
    assert Vacancy.salary_data(vacancy_data) == 50000

    vacancy_data = {
        "salary": {"from": None, "to": 70000}
    }
    assert Vacancy.salary_data(vacancy_data) == 70000

    vacancy_data = {
        "salary": None
    }
    assert Vacancy.salary_data(vacancy_data) == 0

