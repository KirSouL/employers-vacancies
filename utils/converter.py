import json
import csv


class ConvertorFile:
    def __init__(self, path_json: str, path_csv: str) -> None:
        self.path_json = path_json
        self.path_csv = path_csv

    def load_file(self):
        with open(self.path_json, "r", encoding="utf-8") as file:
            return json.load(file)

    def convertion_to_csv(self):

        base_file = self.load_file()
        with open(self.path_csv, mode="w", encoding="utf-8") as file:
            for item in base_file:
                write = csv.DictWriter(file, fieldnames=item.keys())
                write.writeheader()
                write.writerows(base_file)
