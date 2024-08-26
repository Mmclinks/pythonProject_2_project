import pytest

from src.file_connector import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("1", "Python Developer", "https://example.com/1", "Python knowledge required", 120000),
        Vacancy("2", "Java Developer", "https://example.com/2", "Java knowledge required", 110000),
    ]


@pytest.fixture
def json_saver(tmp_path):
    file_path = tmp_path / "hh.json"
    return JSONSaver(file_path=str(file_path))


def test_add_vacancies(json_saver, sample_vacancies):
    json_saver.add_vacancies(sample_vacancies)
    data = json_saver.get_data()

    assert len(data) == 2
    assert data[0]['id'] == "1"
    assert data[1]['id'] == "2"


def test_get_data_empty(json_saver):
    data = json_saver.get_data()
    assert data == []


def test_delete_vacancy(json_saver, sample_vacancies):
    json_saver.add_vacancies(sample_vacancies)
    json_saver.delete_vacancy(1)
    data = json_saver.get_data()

    assert len(data) == 1
    assert data[0]['id'] == "2"


def test_delete_vacancy_not_found(json_saver, sample_vacancies):
    json_saver.add_vacancies(sample_vacancies)
    json_saver.delete_vacancy(3)
    data = json_saver.get_data()

    assert len(data) == 2
