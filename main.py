from src.work_api import ParserEmployer as Empl, ParserEmployerVacancy as EmplVac
from config import path_to_data as path
from connector import config_db
from tqdm import tqdm
from utils.converter import conv
import json
from src.db_manager import DBManager
from src.work_vac import runner
from interface import user_interface

LIST_NAME = ["employers.csv", "logo.csv", "vacancies.csv", "salary.csv", "city.csv", "snippet.csv"]


def main():
    counter = 0

    while counter < 2:
        user_empl = input("Введите название компании работодателя: ").lower()
        path_to_empl = f"{path()}/empl.json"
        empl = Empl(path_to_empl, user_empl)
        empl.load_file()
        empl.save_file()
        counter += 1

    print("Получение данных о вакансиях работодателя...")

    with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
        load_file = json.load(file)

        for item in tqdm(range(0, len(load_file))):
            path_vac = f"{path()}/vac_empl.json"
            vac_empl = EmplVac(path_vac, load_file[item]["id"])
            vac_empl.load_file()
            vac_empl.save_file()

    runner()
    conv()

    db = config_db()
    manager = DBManager(db)
    manager.create_table()

    for name in LIST_NAME:
        path_to_file = f"{path()}/{name}"
        name_table = name.split(".")[0]
        print(manager.load_info_in_table(path_to_file, name_table))

    user_interface(db)


if __name__ == "__main__":
    main()
