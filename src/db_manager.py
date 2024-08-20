from abc import ABC, abstractmethod
import psycopg2
import csv


class ManagerBase(ABC):

    @abstractmethod
    def create_database(self):
        pass

    @abstractmethod
    def del_database(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def del_table(self):
        pass

    @abstractmethod
    def get_companies_and_vacancies_count(self) -> list:
        pass

    @abstractmethod
    def get_all_vacancies(self) -> list:
        pass

    @abstractmethod
    def get_avg_salary(self) -> list:
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self) -> list:
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, keyword: str) -> list:
        pass


class DBManager(ManagerBase):
    """Класс извлекающий информацию из таблиц работодателей и их вакансий"""
    def __init__(self, database: dict) -> None:
        self.host = database["host"]
        self.port = database["port"]
        self.user = database["user"]
        self.password = database["password"]

    def _open_connect(self) -> list:
        """Метод осуществляющий открытие соединения и указателя к базовой БД"""
        auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        conn = psycopg2.connect(host=self.host, port=self.port, user=self.user,
                                password=self.password)
        conn.set_isolation_level(auto_commit)
        cur = conn.cursor()
        return [conn, cur]

    @staticmethod
    def _close_connect(conn, cur) -> list:
        """Метод класса DatabasePostgres осуществляющий закрытие указателя и соединения к БД"""
        cl_cur = cur.close()
        cl_conn = conn.close()
        return [cl_cur, cl_conn]

    def create_database(self) -> None:
        """Метод класса DatabasePostgres осуществляющий создание БД"""
        conn, cur = self._open_connect()

        cur.execute("CREATE DATABASE info_employers;")
        conn.commit()

        self._close_connect(conn, cur)

    def del_database(self) -> None:
        """Метод класса DatabasePostgres осуществляющий удаление БД"""
        conn, cur = self._open_connect()

        cur.execute("DROP DATABASE IF EXISTS info_employers;")
        conn.commit()

        self._close_connect(conn, cur)

    def create_path_to_schema(self) -> None:
        conn, cur = self._open_connect()

        cur.execute("SET search_path TO info_employers;")
        conn.commit()

        self._close_connect(conn, cur)

    def create_table(self) -> None:
        """Метод класса DatabasePostgres осуществляющий формирование таблиц БД"""
        conn, cur = self._open_connect()

        cur.execute(f"CREATE TABLE employers("
                    f"id_employer INT PRIMARY KEY,"
                    f"company_name VARCHAR(100) NOT NULL,"
                    f"url_employer_to_pars TEXT NOT NULL,"
                    f"url_employer TEXT NOT NULL,"
                    f"url_vacancies_employer_to_pars TEXT NOT NULL,"
                    f"open_vacancies int NOT NULL"
                    f");")
        cur.execute(f"CREATE TABLE logo("
                    f"id_logo_company VARCHAR(50) PRIMARY KEY,"
                    f"id_employer INT NOT NULL,"
                    f"picture_original TEXT NOT NULL,"
                    f"picture_240 TEXT NOT NULL,"
                    f"picture_90 TEXT NOT NULL,"
                    f"FOREIGN KEY (id_employer) REFERENCES employers(id_employer)"
                    f");")
        cur.execute(f"CREATE TABLE vacancies("
                    f"id_vacancy INT PRIMARY KEY,"
                    f"id_employer INT NOT NULL,"
                    f"name_vacancy VARCHAR(100) NOT NULL,"
                    f"url_vacancy TEXT NOT NULL,"
                    f"FOREIGN KEY (id_employer) REFERENCES employers(id_employer)"
                    f");")
        cur.execute(f"CREATE TABLE salary("
                    f"id_salary VARCHAR(50) PRIMARY KEY,"
                    f"id_vacancy INT NOT NULL,"
                    f"salary_to INT,"
                    f"salary_from INT,"
                    f"currency VARCHAR(5),"
                    f"gross VARCHAR(5),"
                    f"FOREIGN KEY (id_vacancy) REFERENCES vacancies(id_vacancy)"
                    f");")
        cur.execute(f"CREATE TABLE city("
                    f"id_vacancy_city VARCHAR(50) PRIMARY KEY,"
                    f"id_vacancy INT NOT NULL,"
                    f"id_city VARCHAR(20),"
                    f"name_city VARCHAR(100),"
                    f"url_city_to_pars TEXT,"
                    f"FOREIGN KEY (id_vacancy) REFERENCES vacancies(id_vacancy)"
                    f");")
        cur.execute(f"CREATE TABLE snippet("
                    f"id_snippet VARCHAR(50) PRIMARY KEY,"
                    f"id_vacancy INT NOT NULL,"
                    f"requirement TEXT NOT NULL,"
                    f"responsibility TEXT NOT NULL,"
                    f"FOREIGN KEY (id_vacancy) REFERENCES vacancies(id_vacancy)"
                    f");")

        conn.commit()

        self._close_connect(conn, cur)

    def del_table(self) -> None:
        """Метод класса DatabasePostgres осуществляющий удаление таблиц БД"""
        conn, cur = self._open_connect()

        cur.execute("DROP TABLE employers CASCADE;")
        cur.execute("DROP TABLE IF EXISTS logo;")
        cur.execute("DROP TABLE vacancies CASCADE;")
        cur.execute("DROP TABLE IF EXISTS salary;")
        cur.execute("DROP TABLE IF EXISTS city;")
        cur.execute("DROP TABLE IF EXISTS snippet;")

        conn.commit()

        self._close_connect(conn, cur)

    def load_info_in_table(self, path_to_file_csv: str, table_name: str) -> None:
        """Метод класса DatabasePostgres осуществляющий заполнение данными таблиц БД"""
        conn, cur = self._open_connect()

        with open(path_to_file_csv, newline='', encoding="utf-8") as file:
            reader_csv = csv.reader(file)
            header = next(reader_csv)
            for row in reader_csv:
                query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES" \
                        f"({', '.join(['%s'] * len(row))})"
                cur.execute(query, row)

        conn.commit()

        self._close_connect(conn, cur)

    def get_companies_and_vacancies_count(self) -> list:
        """
        Метод получения списка всех компаний и количества вакансий у каждой компании
        :return all_info: список из наименований компаний и количество вакансий.
        """
        conn, cur = self._open_connect()

        query = f"SELECT DISTINCT(company_name), COUNT(*) as count_vacancy FROM employers" \
                f" JOIN vacancies USING (id_employer)" \
                f" GROUP BY company_name" \
                f" ORDER BY COUNT(*);"
        cur.execute(query)
        conn.commit()
        all_info = cur.fetchall()

        self._close_connect(conn, cur)

        return all_info

    def get_all_vacancies(self) -> list:
        """
        Метод получения списка всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию.
        :return all_info: список из наименований компаний, наименований вакансий, ссылок на вакансии,
                          уровня дохода 'до', уровня дохода 'от'
        """
        conn, cur = self._open_connect()

        query = f"SELECT DISTINCT(company_name), name_vacancy, url_vacancy, salary_to, salary_from" \
                f" FROM employers" \
                f" JOIN vacancies USING (id_employer)" \
                f" JOIN salary USING (id_vacancy);"
        cur.execute(query)
        conn.commit()
        all_info = cur.fetchall()

        self._close_connect(conn, cur)

        return all_info

    def get_avg_salary(self) -> list:
        """
        Метод получения средней зарплаты по вакансиям.
        :return all_info: список из среднего уровня дохода 'до', среднего уровня дохода 'от'
        """
        conn, cur = self._open_connect()

        query = f"SELECT AVG(salary_to), AVG(salary_from) FROM salary;"
        cur.execute(query)
        conn.commit()
        all_info = cur.fetchall()

        self._close_connect(conn, cur)

        return all_info

    def get_vacancies_with_higher_salary(self) -> list:
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        :return all_info: список содержащий обработанную информацию
        """
        conn, cur = self._open_connect()

        query = f"SELECT * FROM vacancies"\
                f" JOIN salary USING (id_vacancy)" \
                f" JOIN employers USING (id_employer)" \
                f" WHERE salary_to > (SELECT AVG(salary_to) FROM salary) AND" \
                f" salary_from > (SELECT AVG(salary_from) FROM salary);"
        cur.execute(query)
        conn.commit()
        all_info = cur.fetchall()

        self._close_connect(conn, cur)

        return all_info

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова
        :return all_info: список содержащий обработанную информацию
        """
        conn, cur = self._open_connect()

        query = f"SELECT * FROM vacancies" \
                f" JOIN salary USING (id_vacancy)" \
                f" JOIN employers USING (id_employer)" \
                f" WHERE name_vacancy LIKE '%{keyword}%';"
        cur.execute(query)
        conn.commit()
        all_info = cur.fetchall()

        self._close_connect(conn, cur)

        return all_info
