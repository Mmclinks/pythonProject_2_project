from typing import Any, Optional


def search_query() -> Any:
    """Функция запрашивает у пользователя ключевое слово и количество вакансий для запроса"""
    user_query = input("Введите поисковый запрос: ")
    try:
        per_pages = int(
            input(
                "Введите количество вакансий для загрузки с сайта. Вакансий на странице(max=100): "
            )
        )
        pages = int(input("Всего страниц: "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка запроса - {e}. Перезапустите программу.")
        return None

    return user_query, pages, per_pages


def filter_data() -> Any:
    """Функция запрашивает у пользователя ключевое слово, уровень зарплаты и топ N для вывода"""
    print("Данные обработаны.")

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")

    salary_input = input("Введите min зарплаты: ")
    if not salary_input:
        salary = 0
    else:
        try:
            salary = int(salary_input)
        except Exception as e:
            print(
                f"Неверный ввод. Ошибка величины зарплаты - {e}. Перезапустите программу."
            )
            return None

    try:
        top_n = int(input("Введите количество вакансий для окончательного вывода: "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка количества - {e}. Перезапустите программу.")
        return None

    return filter_words, salary, top_n


def delete_vacancy() -> Optional[int]:
    """Функция, запрашивающая у пользователя номер вакансии для удаления"""
    try:
        del_number = int(input("Чтобы удалить вакансию, введите id (номер вакансии): "))
    except Exception as e:
        print(f"Неверный ввод. Ошибка при удалении - {e}. Перезапустите программу.")
        return None

    return del_number
