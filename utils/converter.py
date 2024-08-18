import json
import csv
from config import path_to_data as path


class ConvertorFile:
    """Класс ConvertorFile, который преобразует файлы формата json к формату csv"""
    def __init__(self, path_json: str, path_csv: str) -> None:
        self.path_json = path_json
        self.path_csv = path_csv

    def load_file(self):
        """
        Метод класс ConvertorFile открывающий файл формата json
        :return json.load(file): возвращает прочитанный файл формата json"""
        with open(self.path_json, "r", encoding="utf-8") as file:
            return json.loads(file.read())

    def convertion_to_csv(self):
        """Метод класс ConvertorFile записывающий файл формата json в файл формата csv"""
        base_file = self.load_file()
        with open(self.path_csv, "w", newline='', encoding="utf-8") as file:
            write = csv.DictWriter(file, fieldnames=base_file[0].keys())
            write.writeheader()
            for item in base_file:
                write.writerow(item)


def conv():
    """Функция генерации csv файлов"""

    path_j = f"{path()}/base_city.json"
    path_c = f"{path()}/city.csv"

    one = ConvertorFile(path_j, path_c)
    one.convertion_to_csv()

    path_j1 = f"{path()}/base_salary.json"
    path_c1 = f"{path()}/salary.csv"

    one1 = ConvertorFile(path_j1, path_c1)
    one1.convertion_to_csv()

    path_j2 = f"{path()}/base_logo.json"
    path_c2 = f"{path()}/logo.csv"

    one2 = ConvertorFile(path_j2, path_c2)
    one2.convertion_to_csv()

    path_j3 = f"{path()}/base_vacancies.json"
    path_c3 = f"{path()}/vacancies.csv"

    one3 = ConvertorFile(path_j3, path_c3)
    one3.convertion_to_csv()

    path_j4 = f"{path()}/base_employers.json"
    path_c4 = f"{path()}/employers.csv"

    one4 = ConvertorFile(path_j4, path_c4)
    one4.convertion_to_csv()

    path_j5 = f"{path()}/base_snippet.json"
    path_c5 = f"{path()}/snippet.csv"

    one5 = ConvertorFile(path_j5, path_c5)
    one5.convertion_to_csv()
