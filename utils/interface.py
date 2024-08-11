from prettytable import PrettyTable


def user_interface():
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
            additional_parameter = int(input("Введите желаемую стартовую сумму: "))
            print_top("salary_from", additional_parameter, way_to_file)
        elif user_input == "2":
            additional_parameter = int(input("Введите желаемую конечную сумму: "))
            print_top("salary_to", additional_parameter, way_to_file)
        elif user_input == "3":
            additional_parameter = input("Введите желаемый город: ")
            print_top("area", additional_parameter, way_to_file)

        elif user_input == "!":
            print("Подбор завершен")
            user_delete = input("Хотите очистить файл содержащий вакансии?\n"
                                "Это позволит не засорять память Вашего компьютера:)\n"
                                "Введите: да или нет\n")
            if user_delete.lower() == "да":
                del_file = Connector(way_to_file).delete_vacancy()
                print("Завершение работы программы")
                quit()
            else:
                way_to_file = Connector(way_to_file)
                print(f"Файл с вакансиями сохранен. Путь к файлу: {way_to_file.name_file}")
                quit()

def print_top(*args) -> None:
        """
        Функция выводящая результат фильтрации топ вакансий по заданным параметрам
        :param args: набор параметров, на основе которых выдается топ вакансий
        """
        user_ = int(input("Введите количество для топа вакансий: "))
        info = Connector(args[2])
        info_to_user = info.get_info(args[0], args[1])

        table_console = PrettyTable(["name", "url", "salary_from", "salary_to", "currency", "area", "snippet"])

        for vacancy in info_to_user[:user_]:
            table_console.add_row([vacancy["name"], vacancy["url"], vacancy["salary_from"], vacancy["salary_to"],
                                   vacancy["currency"], vacancy["area"], vacancy["snippet"]])

        print(table_console)