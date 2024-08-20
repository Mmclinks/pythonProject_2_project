from abc import ABC, abstractmethod
import requests


class JobAPI(ABC):
    @abstractmethod
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get_vacancies(self, **params):
        """
        Получает вакансии с API сервиса.
        :param params: параметры для запроса вакансий.
        :return: список вакансий.
        """
        pass

    @abstractmethod
    def _make_request(self, endpoint, params):
        """
        Делает запрос к API и возвращает результат.
        :param endpoint: конечная точка API.
        :param params: параметры для запроса.
        :return: данные, полученные от API.
        """
        pass


class HhAPI(JobAPI):
    def __init__(self):
        super().__init__('https://api.hh.ru/')

    def get_vacancies(self, **params):
        endpoint = 'vacancies'
        response = self._make_request(endpoint, params)
        return response.get('items', [])

    def _make_request(self, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Поднимает исключение при наличии ошибки HTTP
        return response.json()
