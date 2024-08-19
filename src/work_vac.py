from abc import ABC, abstractmethod
from config import path_to_data as path
from utils.for_vacancies import EmployerVacancy as EmplVac, SalaryVacancy as SalVac, \
    SnippetVacancy as SnipVac, CityVacancy as CityVac
from utils.for_employers import Employer as Empl, LogoEmployer as LogoEmpl
import json


class GeneratorFileBase(ABC):

    @abstractmethod
    def create_list(self) -> list:
        pass

    @abstractmethod
    def add_file_json(self) -> None:
        pass


class Vacancy(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""

    def __init__(self):
        self.list_vacancy = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса EmployerVacancy
        :return self.list_vacancy: возвращает список экземпляров класса EmployerVacancy
        """
        with open(f"{path()}/vac_empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                empl_vac = EmplVac(item["id"], item["name"], item["alternate_url"], item["employer"]["id"])
                self.list_vacancy.append(empl_vac)

        return self.list_vacancy

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_vacancies.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_vacancy": item.id_vacancy,
                            "id_employer": item.employer_id,
                            "name_vacancy": item.name_vacancy,
                            "url_vacancy": item.url_vacancy})

            json.dump(new, file, indent=4)


class Salary(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""
    def __init__(self):
        self.list_salary = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса SalaryVacancy
        :return self.list_salary: возвращает список экземпляров класса SalaryVacancy
        """
        with open(f"{path()}/vac_empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                sal_vac = SalVac(item["id"], item["salary"])
                self.list_salary.append(sal_vac)
        return self.list_salary

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_salary.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_salary": item.sal_id,
                            "id_vacancy": item.vacancy_id,
                            "salary_to": item.salary_to,
                            "salary_from": item.salary_from,
                            "currency": item.currency,
                            "gross": item.gross})

            json.dump(new, file, indent=4)


class City(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""
    def __init__(self):
        self.list_city = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса CityVacancy
        :return self.list_city: возвращает список экземпляров класса CityVacancy
        """
        with open(f"{path()}/vac_empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                city_vac = CityVac(item["id"], item["area"])
                self.list_city.append(city_vac)

        return self.list_city

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_city.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_vacancy_city": item.city_vac_id,
                            "id_vacancy": item.vacancy_id,
                            "id_city": item.id_city,
                            "name_city": item.city_office,
                            "url_city_to_pars": item.url_city})

            json.dump(new, file, indent=4)


class Snippet(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""
    def __init__(self):
        self.list_snippet = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса SnippetVacancy
        :return self.list_snippet: возвращает список экземпляров класса SnippetVacancy
        """
        with open(f"{path()}/vac_empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                snip_vac = SnipVac(item["id"], item["snippet"]["requirement"],
                                   item["snippet"]["responsibility"])
                self.list_snippet.append(snip_vac)
        return self.list_snippet

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_snippet.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_snippet": item.snip_id,
                            "id_vacancy": item.vacancy_id,
                            "requirement": item.snip_req,
                            "responsibility": item.snip_resp})

            json.dump(new, file, indent=4)


class Employer(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""
    def __init__(self):
        self.list_employer = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса Employer
        :return self.list_employer: возвращает список экземпляров класса Employer
        """
        with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                empl = Empl(item["id"], item["name"], item["url"], item["alternate_url"], item["vacancies_url"],
                            item["open_vacancies"])
                self.list_employer.append(empl)

        return self.list_employer

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_employers.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_employer": item.id_employer,
                            "company_name": item.company,
                            "url_employer_to_pars": item.url_empl_pars,
                            "url_employer": item.url_company,
                            "url_vacancies_employer_to_pars": item.url_vac_pars,
                            "open_vacancies": item.open_vac})

            json.dump(new, file, indent=4)


class Logo(GeneratorFileBase):
    """Класс создающй файл json с новой структурой"""
    def __init__(self):
        self.list_logo_employer = []

    def create_list(self):
        """
        Метод генерирующий список экземляров класса LogoEmployer
        :return self.list_logo_employer: возвращает список экземпляров класса LogoEmployer
        """
        with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
            load_file = json.load(file)
            for item in load_file:
                logo = LogoEmpl(item["id"], item["logo_urls"])
                self.list_logo_employer.append(logo)

        return self.list_logo_employer

    def add_file_json(self):
        """Метод создающий новый json файл"""
        new = []
        load = self.create_list()

        with open(f"{path()}/base_logo.json", "w", encoding="utf-8") as file:
            for item in load:
                new.append({"id_logo_company": item.id_logo,
                            "id_employer": item.id_employer,
                            "picture_original": item.pict_orig,
                            "picture_240": item.pict_240,
                            "picture_90": item.pict_90})

            json.dump(new, file, indent=4)


def runner():
    """Функция запускающая генерацтю json файлов"""
    vac = Vacancy()
    vac.add_file_json()

    sal = Salary()
    sal.add_file_json()

    snip = Snippet()
    snip.add_file_json()

    city = City()
    city.add_file_json()

    empl = Employer()
    empl.add_file_json()

    logo = Logo()
    logo.add_file_json()
