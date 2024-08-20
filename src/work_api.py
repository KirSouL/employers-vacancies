import requests
import json
from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass
            
            
class ParserEmployer(BaseParser):
    """Класс получающий информацию о работодателе по запросу пользователя."""
    employer = []

    def __init__(self, name_file_company: str, name_company: str, max_page: int = 20) -> None:
        self.name_file_company = name_file_company
        self.name_company = name_company
        self.max_page = max_page
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.url_company = f"https://api.hh.ru/employers"

    def load_file(self):
        """ Метод получающий информацию по работодетелю, у которого есть активные вакансии."""
        self.params['text'] = self.name_company

        for param in range(0, self.max_page):
            self.params['page'] = param
            responce = requests.get(self.url_company, headers=self.headers, params=self.params, timeout=10)
            company = responce.json()["items"]
            responce.raise_for_status()

            for item in company:
                if item["open_vacancies"] > 0:
                    ParserEmployer.employer.append(item)
                else:
                    continue

    def save_file(self) -> None:
        """Метод сохраняющий информацию по работодателяю в файл json."""
        with open(self.name_file_company, 'w', encoding='utf-8') as file:
            json.dump(ParserEmployer.employer, file, indent=4)

            
class ParserEmployerVacancy(BaseParser):
    """Класс получающий информацию о вакансиях работодателя"""
    vacancies_employer = []

    def __init__(self, name_file_vacancy: str, id_employer: int, max_page: int = 20) -> None:

        self.name_file_vac = name_file_vacancy
        self.id_empl = id_employer
        self.max_page = max_page
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'page': 0, 'per_page': 100}
        self.url_vac_emp = f"https://api.hh.ru/vacancies?employer_id={self.id_empl}"

    def load_file(self) -> None:
        """Метод получающий информацию о вакансиях работодетеля"""
        while self.params.get('page') != 20:

            responce = requests.get(self.url_vac_emp, headers=self.headers, params=self.params, timeout=10)

            if responce.json()["items"] is []:
                break
            else:
                vacancy = responce.json()["items"]
                ParserEmployerVacancy.vacancies_employer.extend(vacancy)
            self.params['page'] += 1
            
    def save_file(self):
        """Метод сохраняющий информацию о вакансиях работодателя в файл json."""
        with open(self.name_file_vac, "w", encoding="utf-8") as file:
            json.dump(self.vacancies_employer, file)
