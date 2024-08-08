import requests
import json
from config import path_to_data as path
from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    
# class ParserVacancy(BaseParser):
#     def __init__(self, name_file_vacancy: str, name_vacancy: str):
#         self.name_file_vac = name_file_vacancy
#         self.name_vacancy = name_vacancy
#         self.headers = {'User-Agent': 'HH-User-Agent'}
#         self.params = {'text': '', 'page': 0, 'per_page': 100}
#         self.url_vac = "https://api.hh.ru/vacancies"
#         self.vacancy = []
#
#     def __str__(self):
#         return f"employer: "
#
#     def load_file(self):
#
#         self.params['text'] = self.name_vacancy
#         while self.params.get('page') != 20:
#             responce = requests.get(self.url_vac, headers=self.headers, params=self.params, timeout=10)
#             vacancies = responce.json()
#             self.vacancy.extend(vacancies)
#             self.params['page'] += 1
#
#     def save_file(self):
#         with open(self.name_file_vac, 'w', encoding='utf-8') as file:
#             json.dump(self.vacancy, file, indent=4)
            
            
class ParserEmployer(BaseParser):
    employer = []

    def __init__(self, name_file_company: str, name_company: str):
        self.name_file_company = name_file_company
        self.name_company = name_company
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.url_company = f"https://api.hh.ru/employers"

    def load_file(self):
        
        self.params['text'] = self.name_company
        while self.params.get('page') != 20:
            responce = requests.get(self.url_company, headers=self.headers, params=self.params, timeout=10)
            company = responce.json()['items']
            for item in company:
                if item["open_vacancies"] > 0:
                    ParserEmployer.employer.append(item)
            self.params['page'] += 1
            
    def save_file(self) -> None:
        with open(self.name_file_company, 'w', encoding='utf-8') as file:
            json.dump(ParserEmployer.employer, file, indent=4)

            
class ParserEmployerVacancy(BaseParser):

    def __init__(self, name_file_vacancy: str, id_employer: int) -> None:
        self.name_file_vac = name_file_vacancy
        self.id_empl = id_employer
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'page': 0, 'per_page': 100}
        self.params_emp = {'page': 0, 'per_page': 100}
        self.url_vac_emp = f"https://api.hh.ru/vacancies?employer_id={self.id_empl}"
        self.vacancies_employer = []
    
    def load_file(self) -> None:

        while self.params.get('page') != 20:
            responce = requests.get(self.url_vac_emp, headers=self.headers, params=self.params, timeout=10)
            vacancy = responce.json()["items"]
            self.vacancies_employer.extend(vacancy)
            self.params['page'] += 1
            
    def save_file(self):
        with open(self.name_file_vac, "w", encoding="utf-8") as file:
            json.dump(self.vacancies_employer, file, indent=4)


def run_():
    counter = 0

    while counter < 1:
        user_empl = input("Введите работодателя: ").lower()
        path_to_empl = f"{path()}/empl.json"
        empl = ParserEmployer(path_to_empl, user_empl)
        empl.load_file()
        empl.save_file()
        counter += 1

    with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
        load_file = json.load(file)

        for item in load_file:
            path_vac = f"{path()}/vac_empl.json"
            vac_empl = ParserEmployerVacancy(path_vac, item["id"])
            vac_empl.load_file()
            vac_empl.save_file()


run_()
