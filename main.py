from src.work_api import ParserEmployer as Empl, ParserEmployerVacancy as EmplVac
from config import path_to_data as path
from connector import config_db
from utils.converter import conv
import json
from src.db_manager import DBManager
from src.work_vac import runner
from interface import user_interface

LIST_NAME = ["employers.csv", "logo.csv", "vacancies.csv", "salary.csv", "city.csv", "snippet.csv"]


def main():

    with open(f"{path()}/list_employers.json", "r", encoding="utf-8") as file:
        load_list_employers = json.load(file)

        for company in load_list_employers:
            path_to_empl = f"{path()}/empl.json"
            empl = Empl(path_to_empl, company)
            empl.load_file()
            empl.save_file()

    print("Получение данных о вакансиях работодателя...")

    with open(f"{path()}/empl.json", "r", encoding="utf-8") as file:
        load_file = json.load(file)

        for item in range(0, len(load_file)):
            path_vac = f"{path()}/vac_empl.json"
            vac_empl = EmplVac(path_vac, load_file[item]["id"])
            vac_empl.load_file()
            vac_empl.save_file()

    runner()
    conv()

    db = config_db()
    manager = DBManager(db)
    try:
        manager.create_table()
    except:
        print("Таблицы в БД ранее были созданы. Сейчас всё исправим.")
        manager.del_table()
        manager.create_table()

    for name in LIST_NAME:
        path_to_file = f"{path()}/{name}"
        name_table = name.split(".")[0]
        manager.load_info_in_table(path_to_file, name_table)

    user_interface(db)


if __name__ == "__main__":
    main()
