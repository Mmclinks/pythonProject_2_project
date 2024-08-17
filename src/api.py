from abc import ABC, abstractmethod
import requests

class JobAPI(ABC):
    @abstractmethod
    def fetch_vacancies(self, text: str, area: int, pages: int):
        pass

class HHAPI(JobAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_vacancies(self, text: str, area: int = 1, pages: int = 1):
        vacancies = []
        params = {'text': text, 'area': area, 'per_page': 100}
        for page in range(pages):
            params['page'] = page
            response = requests.get(self.url, headers=self.headers, params=params)
            if response.status_code == 200:
                vacancies.extend(response.json()['items'])
            else:
                print(f"Failed to fetch data: {response.status_code}")
        return vacancies
