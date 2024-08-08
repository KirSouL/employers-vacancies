from config import path_to_data as path
from src.work_api import ParserEmployer as Empl, ParserEmployerVacancy as EmplVac
import json


def main():
    counter = 0

    while counter < 1:
        user_empl = input("Введите работодателя: ").lower()
        path_to_empl = f"{path()}/empl.json"
        empl = Empl(path_to_empl, user_empl)
        empl.load_file()
        empl.save_file()
        counter += 1

    with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
        load_file = json.load(file)

        for item in load_file:
            path_vac = f"{path()}/vac_empl.json"
            vac_empl = EmplVac(path_vac, item["id"])
            vac_empl.load_file()
            vac_empl.save_file()


if __name__ == "__main__":
    main()
