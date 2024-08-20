from prettytable import PrettyTable
from src.db_manager import DBManager


def user_interface(database: dict):
    """
    Функция для работы с пользователем
    """
    while True:
        print(
            "Введите какой результат хотите получить:\n"
            "1. Информация о всех компаниях и количество вакансий у каждой из них\n"
            "2. Информация о всех вакансиях с указанием названия компанииь названия вакансии,"
            "зарплаты и ссылки на вакансию\n"
            "3. Информация о средней зарплате по вакансиям\n"
            "4. Информация о всех вакансиях, у которых зарплата выше средней по всем вакансиям\n"
            "5. Информация о всех вакансиях, в названии которых содержатся переданные слова\n"
            "!. Завершение работы\n"
        )
        user_input = str(input("Введите операцию: "))

        if user_input == "1":
            list_name = []
            list_count_vacancies = []

            employers_and_open_vacancy = DBManager(database)
            info = employers_and_open_vacancy.get_companies_and_vacancies_count()
            table_console = PrettyTable(["company_name", "open_vacancies"])

            for item in info:
                list_name.append(item[0])
                list_count_vacancies.append(item[1])

            for item in range(len(info)):
                table_console.add_row([list_name[item], list_count_vacancies[item]])

            print(table_console)

        elif user_input == "2":
            list_company = []
            list_vacancies = []
            list_url_vac = []
            list_sal_to = []
            list_sal_from = []

            employers_and_open_vacancy = DBManager(database)
            info = employers_and_open_vacancy.get_all_vacancies()
            table_console = PrettyTable(["company_name", "name_vacancy", "url_vacancy", "salary_to", "salary_from"])

            for item in info:
                list_company.append(item[0])
                list_vacancies.append(item[1])
                list_url_vac.append(item[2])
                list_sal_to.append(item[3])
                list_sal_from.append(item[4])

            for item in range(len(info)):
                table_console.add_row([list_company[item], list_vacancies[item], list_url_vac[item],
                                       list_sal_to[item], list_sal_from[item]])

            print(table_console)

        elif user_input == "3":
            list_average_salary_to = []
            list_average_salary_from = []

            employers_and_open_vacancy = DBManager(database)
            info = employers_and_open_vacancy.get_avg_salary()
            table_console = PrettyTable(["average_salary_to", "average_salary_from"])

            for item in info:
                list_average_salary_to.append(item[0])
                list_average_salary_from.append(item[1])

            for item in range(len(info)):
                table_console.add_row([round(list_average_salary_to[item]), round(list_average_salary_from[item])])

            print(table_console)

        elif user_input == "4":
            list_company = []
            list_name_vacancy = []
            list_salary_to = []
            list_salary_from = []

            employers_and_open_vacancy = DBManager(database)
            info = employers_and_open_vacancy.get_vacancies_with_higher_salary()
            table_console = PrettyTable(["company_name", "name_vacancy", "salary_to", "salary_from"])

            for item in info:
                list_company.append(item[9])
                list_name_vacancy.append(item[2])
                list_salary_to.append(item[5])
                list_salary_from.append(item[6])

            for item in range(len(info)):
                table_console.add_row([list_company[item], list_name_vacancy[item], list_salary_to[item],
                                       list_salary_from[item]])

            print(table_console)

        elif user_input == "5":
            list_company = []
            list_name_vacancy = []
            list_salary_to = []
            list_salary_from = []
            list_url_employer = []
            list_url_vacancy = []
            list_currency = []
            keyword = input("Введите слово, которое должно содержатся в вакаснсии: ")
            employers_and_open_vacancy = DBManager(database)
            info = employers_and_open_vacancy.get_vacancies_with_keyword(keyword)
            table_console = PrettyTable(["company_name", "url_company", "name_vacancy", "url_vacancy",
                                         "salary_to", "salary_from", "currency"])

            for item in info:
                list_company.append(item[9])
                list_name_vacancy.append(item[2])
                list_salary_to.append(item[5])
                list_salary_from.append(item[6])
                list_url_employer.append(item[11])
                list_url_vacancy.append(item[3])
                list_currency.append(item[7])

            for item in range(len(info)):
                table_console.add_row([list_company[item], list_url_employer[item], list_name_vacancy[item],
                                       list_url_vacancy[item], list_salary_to[item], list_salary_from[item],
                                       list_currency[item]])

            print(table_console)

        elif user_input == "!":

            print("Работа завершена. Заходите ещё)")

            quit()
