import pytest
from config import path_to_utils as path_ut
from utils.for_vacancies import Vacancy as Vac, SalaryVacancy as Sal, SnippetVacancy as Snip, CityVacancy as City

vac_1 = Vac(123, "test", "https://test.ru",  1564)
vac_2 = Vac(1023, "test2", "https://test.ru",  1565)

sal_1 = Sal(vac_1.salary_id, {"to": 100000, "from": 150000, "currency": "RUR", "gross": True})
sal_2 = Sal(vac_2.salary_id, None)

print(sal_1)
print(sal_2)

snip_1 = Snip(vac_1.snippet_id, "little info", "more info")
snip_2 = Snip(vac_2.snippet_id, "more little info", "more more info")
snip_3 = Snip(vac_1.snippet_id, "more little info", "more more info")

print(snip_1)
print(snip_2)
print(snip_3)

ci_1 = City(vac_1.city_id, None)
ci_2 = City(vac_2.city_id, {"id": 21, "name": "SPb", "url": "https://city.ru"})

print(ci_1)
print(ci_2)