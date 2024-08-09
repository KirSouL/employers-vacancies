import psycopg2
import csv
import json
from config import path_to_data as path
from abc import ABC, abstractmethod


class BaseTable(ABC):

    @abstractmethod
    def load_file(self) -> list[dict]:
        pass

    @abstractmethod
    def conversion_file(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class TablePostgres(BaseTable):

    def __init__(self, path_to_file_json: str, path_to_file_csv: str):
        self.path = path_to_file_json
        self.path_csv = path_to_file_csv

    def load_file(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def conversion_file(self):
        base_file = self.load_file()
        with open(self.path_csv, mode="w", encoding="utf-8") as file:
            counter = 0
            for item in base_file:
                if item.keys() == "logo_urls":
                    self.logo()
                    item["logo_urls"] = counter
                    counter += 1

                write = csv.DictWriter(file, fieldnames=item.keys())
                write.writeheader()
                write.writerows(base_file)

    def logo(self):
        pass

    def create_table(self):
        pass


def runer():
    path_one = f"{path()}/empl.json"
    path_two = f"{path()}/employers.csv"
    table_ = TablePostgres(path_one, path_two)
    table_.load_file()
    table_.conversion_file()
    # table_.conversion_file()


print(runer())
