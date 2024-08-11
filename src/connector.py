import psycopg2
from configparser import ConfigParser as ConfPars


class ConnectorPSQL:
    connection = None
    cursor = None

    def __init__(self) -> None:
        parser = ConfPars()
        parser.read("database.ini")

        database = {}
        params = parser.items("postgresql")

        for param in params:
            database[param[0]] = param[1]

        connect = psycopg2.connect(**database)
        ConnectorPSQL.connection = connect
        ConnectorPSQL.cursor = connect.cursor()

    def request_action(self, string: str, params: dict):
        result = None

        if params:
            ConnectorPSQL.cursor.execute(string, params)
        else:
            ConnectorPSQL.cursor.execute(params)

        if ConnectorPSQL.cursor.description is not None:
            result = ConnectorPSQL.cursor.fetchone()

        ConnectorPSQL.connection.commit()

        return result





def connect_to_psql(user_host: str, user_port: str, user_database: str, user_name: str,
                    user_password: str) -> None:
    connect = psycopg2.connect(
        host=f"{user_host}",
        port=f"{user_port}",
        user=f"{user_name}",
        password=f"{user_password}"
    )
    curs = connect.cursor()
    curs.execute("CREATE DATABASE employers and vacancies;")
    curs.execute("DROP TABLE employers;")
    curs.execute("CREATE TABLE employers (employer_id CHAR(5) PRIMARY KEY, company_name VARCHAR(100) NOT NULL, contact_name varchar(100) NOT NULL);")
    connect.commit()
    info = f"INSERT INTO customers VALUES(12540, 'Power', 'Petro') returning *"
    curs.execute(info)
    connect.commit()
    cur_cust = curs.fetchall()
    curs.close()
    connect.close()
    return cur_cust





def cont(user_host: str, user_port: str, user_database: str, user_name: str, user_password: str) -> None:
    connect = psycopg2.connect(
        host=f"{user_host}",
        port=f"{user_port}",
        user=f"{user_name}",
        password=f"{user_password}"
    )
    curs = connect.cursor()
    curs.execute("DROP TABLE employers;")
    connect.commit()
    curs.close()
    connect.close()



