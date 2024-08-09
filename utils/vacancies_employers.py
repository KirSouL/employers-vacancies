
class Vacancy:
    """Класс Vacancy формирующий новую структуру для JSON файла вакансий с сайта hh.ru"""
    def __init__(self, id_vacancy: int, name_vacancy: str, url_vacancy: str, city: str | None,
                 employer_id: int) -> None:
        self.id_vacancy = id_vacancy
        self.salary_id = f"sal{self.id_vacancy}"
        self.snippet_id = f"snip{self.id_vacancy}"
        self.employer_id = employer_id
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.city = self.__val_city(city)
        # self.salary_from = self._validate_salary(self.unpacking_dict(salary_dict)[0])
        # self.salary_to = self._validate_salary(self.unpacking_dict(salary_dict)[1])
        # self.salary_currency = self.__val_currency(self.unpacking_dict(salary_dict)[2])
        # self.snippet_requirement = snippet_requirement



    # @classmethod
    # def unpacking_dict(cls, salary_dict):
    #     if type(salary_dict) is dict:
    #         salary_from, salary_to, currency, gross = salary_dict.values()
    #         return salary_from, salary_to, currency, gross
    #     raise TypeError("Ошибка типа данных: данные по заработной плате отсутствуют")

    @staticmethod
    def __val_city(city):
        if city is None:
            city = "Город не указан"
        else:
            city = city

        return city

    @staticmethod
    def _validate_salary(salary):
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        :param salary: зарплата передававемая при инициализации, либо salary_to, либо salary_from
        """
        if salary is None:
            salary = 0
        else:
            salary = salary
        return salary



    def __str__(self):
        return (f"Наименование вакансии: {self.name_vacancy} \n"
                f"Город, в котором расположен офис компании: {self.city} \n"
                f"Заработная плата: от {self.salary_from} - до {self.salary_to} {self.salary_currency} \n"
                f"Описание вакансии: {self.snippet_requirement}")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name_vacancy}, {self.url_vacancy}, {self.city}, "
                f"{self.salary_to}, {self.salary_from}, {self.salary_currency}, {self.snippet_requirement})")

    def __le__(self, other):
        if self.salary_to and other.salary_to:
            return self.salary_to <= other.salary_to

        if self.salary_from and other.salary_from:
            return self.salary_from <= other.salary_from


class Salary:

    # def unpacking(self, salary: dict | None) -> None:
    #     if type(salary) is dict:
    #         pass
    def __init__(self, salary_id: str, salary: dict | None) -> None:
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.sal_id = salary_id
        self.salary_to = self._validate_salary(salary["to"])
        self.salary_from = self._validate_salary(salary["from"])
        self.currency = self.__val_currency(salary["currency"])

    @staticmethod
    def _validate_salary(salary):
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        :param salary: зарплата передававемая при инициализации, либо salary_to, либо salary_from
        """
        if salary is None:
            salary = 0
        else:
            salary = salary
        return salary

    @staticmethod
    def __val_currency(currency):
        if currency is not None:
            currency = currency
        else:
            currency = 'Валюта не указана'

        return currency


class Snippet:

    def __init__(self, snippet_id: str, snippet_requirement: str, snippet_responsibility: str) -> None:
        self.snip_id = snippet_id
        self.snip_req = snippet_requirement
        self.snip_resp = snippet_responsibility
