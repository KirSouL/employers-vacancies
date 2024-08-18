class EmployerVacancy:
    """Класс EmployerVacancy формирующий новую структуру для JSON файла вакансий работодателя с сайта hh.ru"""

    def __init__(self, id_vacancy: str, name_vacancy: str, url_vacancy: str, employer_id: str) -> None:
        self.id_vacancy = int(id_vacancy)
        self.employer_id = int(employer_id)
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy

    def __str__(self):
        return (f"ID вакансии: {self.id_vacancy}\n"
                f"ID работодателя: {self.employer_id}\n"
                f"Наименование вакансии: {self.name_vacancy}\n"
                f"URL ссылка на вакансию: {self.url_vacancy}\n")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.id_vacancy}, {self.name_vacancy}, {self.url_vacancy},"
                f"{self.employer_id})")


class CityVacancy:
    """Класс CityVacancy формирующий новую структуру для JSON файла вакансий работодателя с сайта hh.ru"""

    def __init__(self, city_vacancy_id: str, city: dict and None) -> None:
        self.city_vac_id = f"city{city_vacancy_id}"
        self.vacancy_id = int(city_vacancy_id)
        self.id_city = self._city(city)[0]
        self.city_office = self._city(city)[1]
        self.url_city = self._city(city)[2]

    def __str__(self):
        return (f"{self.__class__.__name__}(\n"
                f"'id_city_vacancy': {self.city_vac_id},\n"
                f"'id_vacancy': {self.vacancy_id},\n"
                f"'id_city': {self.id_city},\n"
                f"'name': {self.city_office},\n"
                f"'url': {self.url_city}\n"
                f")")

    @staticmethod
    def _city(city: dict and None) -> list:
        """
        Метод обрабатывающий информацию о месте расположения компании.
        :param city: информация о оффисе
        :return list_city_info: список параметров места расположения компании
        """
        list_city_info = []

        if not isinstance(city, dict):
            id_city, city_office, url_city = None, None, None
        else:
            id_city, city_office, url_city = city.values()

        list_city_info.extend((id_city, city_office, url_city))

        return list_city_info


class SalaryVacancy:
    """Класс SalaryVacancy формирующий новую структуру для JSON файла вакансий работодателя с сайта hh.ru"""

    def __init__(self, salary_id: str, salary: dict and None) -> None:
        self.sal_id = f"sal{salary_id}"
        self.vacancy_id = int(salary_id)
        if not isinstance(salary, dict):
            self.salary_to = 0
            self.salary_from = 0
            self.currency = None
            self.gross = None
        else:
            self.salary_to = self._unpacking_salary(salary["to"])
            self.salary_from = self._unpacking_salary(salary["from"])
            self.currency = self.__unpacking_currency(salary["currency"])
            self.gross = self._validate_gross(salary["gross"])

    def __str__(self):
        return (f"{self.__class__.__name__}(\n"
                f"'id_salary': {self.sal_id},\n"
                f"'id_vacancy': {self.vacancy_id},\n"
                f"'salary_to': {self.salary_to},\n"
                f"'salary_from': {self.salary_from},\n"
                f"'currency': {self.currency},\n"
                f"'gross': {self.gross}\n"
                f")")

    @staticmethod
    def _unpacking_salary(salary: int and None) -> int:
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        :param salary: зарплата передававемая при инициализации, либо salary_to, либо salary_from
        :return salary: возвращает обработанную зарплату
        """
        if salary is None:
            salary = 0
        else:
            salary = salary

        return salary

    @staticmethod
    def __unpacking_currency(currency: str and None) -> str and None:
        """
        Метод класса осуществляющий валидацию валюты вакансий
        :param currency : валюта передававемая при инициализации
        :return currency: возвращает обработанную валюту
        """
        if currency is not None:
            currency = currency
        else:
            currency = None

        return currency

    @staticmethod
    def _validate_gross(gross: bool) -> int:
        """
        Метод класса осуществляющий валидацию логического состояние ЗП (с учетом вычета налога или нет) вакансий
        :param gross : состояние ЗП передававемая при инициализации
        :return gross: возвращает обработанную состояние ЗП
        """
        if gross is True:
            gross = 1
        else:
            gross = 0

        return gross


class SnippetVacancy:
    """Класс SnippetVacancy формирующий новую структуру для JSON файла вакансий работодателя с сайта hh.ru"""
    def __init__(self, snippet_id: str, snippet_requirement: str, snippet_responsibility: str) -> None:
        self.snip_id = f"snip{snippet_id}"
        self.vacancy_id = int(snippet_id)
        self.snip_req = snippet_requirement
        self.snip_resp = snippet_responsibility

    def __repr__(self):
        return f"{self.__class__.__name__}({self.snip_id}, {self.vacancy_id}, {self.snip_req}, {self.snip_resp})"
