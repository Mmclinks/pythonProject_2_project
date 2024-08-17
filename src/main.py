from api import HHAPI
from vacancy import Vacancy
from storage import JSONJobStorage


def user_interaction():
    hh_api = HHAPI()
    storage = JSONJobStorage()

    while True:
        print("\n1. Запросить вакансии с hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Добавить вакансию")
        print("5. Удалить вакансию")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            text = input("Введите поисковый запрос: ")
            pages = int(input("Введите количество страниц для запроса: "))
            vacancies = hh_api.fetch_vacancies(text=text, pages=pages)
            for vac in vacancies:
                vacancy = Vacancy(
                    name=vac['name'],
                    url=vac['alternate_url'],
                    salary_from=vac['salary']['from'] if vac['salary'] else None,
                    salary_to=vac['salary']['to'] if vac['salary'] else None,
                    description=vac['snippet']['requirement']
                )
                storage.add_vacancy(vacancy)
            print(f"Добавлено {len(vacancies)} вакансий")

        elif choice == '2':
            n = int(input("Введите количество вакансий: "))
            sorted_vacancies = sorted(storage.vacancies, key=lambda x: x.salary_from, reverse=True)
            for vac in sorted_vacancies[:n]:
                print(vac)

        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            filtered_vacancies = storage.get_vacancies(description=keyword)
            for vac in filtered_vacancies:
                print(vac)

        elif choice == '4':
            name = input("Введите название вакансии: ")
            url = input("Введите ссылку на вакансию: ")
            salary_from = input("Введите начальную зарплату: ")
            salary_to = input("Введите конечную зарплату: ")
            description = input("Введите описание вакансии: ")
            vacancy = Vacancy(
                name=name,
                url=url,
                salary_from=int(salary_from) if salary_from else None,
                salary_to=int(salary_to) if salary_to else None,
                description=description
            )
            storage.add_vacancy(vacancy)
            print("Вакансия добавлена")

        elif choice == '5':
            name = input("Введите название вакансии для удаления: ")
            storage.delete_vacancies(name=name)
            print("Вакансия удалена")

        elif choice == '6':
            break

        else:
            print("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    user_interaction()
