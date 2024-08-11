
class Vacancy:
    """Класс Vacancy формирующий новую структуру для JSON файла вакансий работодателя с сайта hh.ru"""
    def __init__(self, id_vacancy: str, name_vacancy: str, url_vacancy: str, employer_id: str) -> None:
        self.id_vacancy = id_vacancy
        self.salary_id = f"sal{self.id_vacancy}"
        self.snippet_id = f"snip{self.id_vacancy}"
        self.employer_id = employer_id
        self.city_id = f"cv{self.id_vacancy}"
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy

    def __str__(self):
        return (f"ID вакансии: {self.id_vacancy}\n"
                f"ID заработной платы: {self.salary_id}\n"
                f"ID описания вакансии: {self.snippet_id}\n"
                f"ID работодателя: {self.employer_id}\n"
                f"Наименование вакансии: {self.name_vacancy}\n"
                f"URL ссылка на вакансию: {self.url_vacancy}\n")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.id_vacancy}, {self.name_vacancy}, {self.url_vacancy},"
                f"{self.employer_id})")


class CityVacancy:
    def __init__(self, city_vacancy_id: str, city: dict | None) -> None:
        self.city_vac_id = city_vacancy_id
        self.id_city = self._city(city)[0]
        self.city_office = self._city(city)[1]
        self.url_city = self._city(city)[2]

    def __str__(self):
        return (f"{self.__class__.__name__}({self.city_vac_id},\n"
                f"'id': {self.id_city},\n"
                f"'name': {self.city_office},\n"
                f"'url': {self.url_city})")

    @staticmethod
    def _city(city: dict | None) -> list:
        list_city_info = []

        if not isinstance(city, dict):
            id_city, city_office, url_city = None, None, None
        else:
            id_city, city_office, url_city = city.values()

        list_city_info.extend((id_city, city_office, url_city))

        return list_city_info


class SalaryVacancy:

    def __init__(self, salary_id: str, salary: dict | None) -> None:
        self.sal_id = salary_id
        if not isinstance(salary, dict):
            self.salary_to = None
            self.salary_from = None
            self.currency = None
            self.gross = None
        else:
            self.salary_to = self._unpacking_salary(salary["to"])
            self.salary_from = self._unpacking_salary(salary["from"])
            self.currency = self.__unpacking_currency(salary["currency"])
            self.gross = salary["gross"]

    def __str__(self):
        return (f"{self.__class__.__name__}({self.sal_id},\n"
                f"'salary_to': {self.salary_to },\n"
                f"'salary_from': {self.salary_from},\n"
                f"'currency': {self.currency},\n"
                f"'gross': {self.gross}})")

    @staticmethod
    def _unpacking_salary(salary: int | None) -> int | None:
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        :param salary: зарплата передававемая при инициализации, либо salary_to, либо salary_from
        """
        if salary is None:
            salary = None
        else:
            salary = salary

        return salary

    @staticmethod
    def __unpacking_currency(currency: str | None) -> str | None:
        if currency is not None:
            currency = currency
        else:
            currency = None

        return currency


class SnippetVacancy:

    def __init__(self, snippet_id: str, snippet_requirement: str, snippet_responsibility: str) -> None:
        self.snip_id = snippet_id
        self.snip_req = snippet_requirement
        self.snip_resp = snippet_responsibility

    def __repr__(self):
        return f"{self.__class__.__name__}({self.snip_id}, {self.snip_req}, {self.snip_resp})"
