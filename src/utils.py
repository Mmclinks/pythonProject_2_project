def format_salary(salary):
    """Форматирование информации о зарплате"""
    salary_from = salary.get('from', 'не указано')
    salary_to = salary.get('to', 'не указано')
    currency = salary.get('currency', '')
    return f"от {salary_from} до {salary_to} {currency}"
