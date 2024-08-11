class Employer:

    def __init__(self, id_employer: str, company_name: str, url_employers_to_pars: str, url_company: str,
                 url_vacancies_to_pars: str, open_vacancies: int) -> None:
        self.id_employer = id_employer
        self.logo_id = f"empl{self.id_employer}"
        self.company = company_name
        self.url_empl_pars = url_employers_to_pars
        self.url_company = url_company
        self.url_vac_pars = url_vacancies_to_pars
        self.open_vac = open_vacancies

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}({self.id_employer}, {self.company}, {self.url_empl_pars},"
                f"{self.url_company}, {self.url_vac_pars}, {self.open_vac})")


class LogoEmployer:

    def __init__(self, id_logo: str, picture_original: str, picture_240: str, picture_90: str) -> None:
        self.id_logo = id_logo
        self.pict_orig = picture_original
        self.pict_240 = picture_240
        self.pict_90 = picture_90

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id_logo}, {self.pict_orig}, {self.pict_240}, {self.pict_90})"
