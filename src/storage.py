from abc import ABC, abstractmethod
import json
from vacancy import Vacancy

class JobStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **criteria):
        pass

    @abstractmethod
    def delete_vacancies(self, **criteria):
        pass

class JSONJobStorage(JobStorage):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename
        self.vacancies = self.load_vacancies()

    def load_vacancies(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [Vacancy(**vac) for vac in json.load(file)]
        except FileNotFoundError:
            return []

    def save_vacancies(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([vac.__dict__ for vac in self.vacancies], file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, **criteria):
        vacancies = self.vacancies
        for key, value in criteria.items():
            vacancies = [vac for vac in vacancies if getattr(vac, key) == value]
        return vacancies

    def delete_vacancies(self, **criteria):
        for key, value in criteria.items():
            self.vacancies = [vac for vac in self.vacancies if getattr(vac, key) != value]
        self.save_vacancies()
