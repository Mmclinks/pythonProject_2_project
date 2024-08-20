import pytest
from src.utils import format_salary

def test_format_salary_full_data():
    salary = {
        'from': 50000,
        'to': 70000,
        'currency': 'RUR'
    }
    expected = "от 50000 до 70000 RUR"
    assert format_salary(salary) == expected

def test_format_salary_no_from():
    salary = {
        'to': 70000,
        'currency': 'RUR'
    }
    expected = "от не указано до 70000 RUR"
    assert format_salary(salary) == expected

def test_format_salary_no_to():
    salary = {
        'from': 50000,
        'currency': 'RUR'
    }
    expected = "от 50000 до не указано RUR"
    assert format_salary(salary) == expected

def test_format_salary_no_currency():
    salary = {
        'from': 50000,
        'to': 70000,
    }
    expected = "от 50000 до 70000 "
    assert format_salary(salary) == expected

def test_format_salary_no_from_to_currency():
    salary = {}
    expected = "от не указано до не указано "
    assert format_salary(salary) == expected
