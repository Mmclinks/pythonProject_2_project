from src.api import HhAPI
from src.utils import format_salary


def search_vacancies(hh_api):
    query = input("Введите поисковый запрос: ")
    per_page = int(input("Сколько вакансий показать (по умолчанию 10): ") or 10)

    vacancies = hh_api.get_vacancies(text=query, per_page=per_page)

    if vacancies:
        print(f"\nНайдено {len(vacancies)} вакансий:")
        for idx, vacancy in enumerate(vacancies, 1):
            salary = vacancy.get('salary')
            salary_info = format_salary(salary) if salary else "Зарплата не указана"
            print(f"{idx}. {vacancy['name']} ({vacancy['employer']['name']}) - {salary_info}")
    else:
        print("Вакансий не найдено.")


def get_top_n_vacancies(hh_api):
    query = input("Введите поисковый запрос для поиска: ")
    n = int(input("Сколько вакансий показать в топе: "))

    vacancies = hh_api.get_vacancies(text=query, per_page=100)

    if vacancies:
        vacancies_with_salary = [v for v in vacancies if v.get('salary') and v['salary'].get('from')]
        sorted_vacancies = sorted(vacancies_with_salary, key=lambda v: v['salary']['from'], reverse=True)

        print(f"\nТоп {n} вакансий по зарплате:")
        for idx, vacancy in enumerate(sorted_vacancies[:n], 1):
            salary = vacancy['salary']
            salary_info = format_salary(salary)
            print(f"{idx}. {vacancy['name']} ({vacancy['employer']['name']}) - {salary_info}")
    else:
        print("Вакансий не найдено.")


def find_vacancies_by_keyword(hh_api):
    keyword = input("Введите ключевое слово для поиска в описании: ").lower()

    vacancies = hh_api.get_vacancies(per_page=100)

    matched_vacancies = [
        v for v in vacancies
        if (v['snippet'].get('responsibility') and keyword in v['snippet']['responsibility'].lower()) or
           (v['snippet'].get('requirement') and keyword in v['snippet']['requirement'].lower()) or
           (v['name'].lower() and keyword in v['name'].lower())
    ]

    if matched_vacancies:
        print(f"\nНайдено {len(matched_vacancies)} вакансий с ключевым словом '{keyword}':")
        for idx, vacancy in enumerate(matched_vacancies, 1):
            salary = vacancy.get('salary')
            salary_info = format_salary(salary) if salary else "Зарплата не указана"
            print(f"{idx}. {vacancy['name']} ({vacancy['employer']['name']}) - {salary_info}")
    else:
        print(f"Вакансий с ключевым словом '{keyword}' не найдено.")


def save_vacancies_to_file(vacancies, filename="vacancies.json"):
    import json
    with open(filename, 'w') as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=4)
    print(f"Вакансии сохранены в файл {filename}")


def user_interaction():
    hh_api = HhAPI()

    while True:
        print("\nДобро пожаловать в сервис поиска вакансий!")
        print("Выберите действие:")
        print("1. Ввести поисковый запрос и получить вакансии")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Найти вакансии с ключевым словом в описании")
        print("4. Сохранить найденные вакансии в файл")
        print("5. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == "1":
            search_vacancies(hh_api)
        elif choice == "2":
            get_top_n_vacancies(hh_api)
        elif choice == "3":
            find_vacancies_by_keyword(hh_api)
        elif choice == "4":
            vacancies = hh_api.get_vacancies(per_page=100)
            save_vacancies_to_file(vacancies)
        elif choice == "5":
            print("Спасибо за использование сервиса. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
