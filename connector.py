import psycopg2
from configparser import ConfigParser as ConfPars


def config_db(filename="database.ini", section="postgresql"):

    parser = ConfPars()
    parser.read(filename)

    database = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(section, filename)
        )

    return database


# def connect_to_psql(user_host: str, user_port: str, user_database: str, user_name: str,
#                     user_password: str) -> None:
#     connect = psycopg2.connect(
#         host=f"{user_host}",
#         port=f"{user_port}",
#         user=f"{user_name}",
#         password=f"{user_password}"
#     )
#     curs = connect.cursor()
#     curs.execute("CREATE DATABASE employers and vacancies;")
#     curs.execute("DROP TABLE employers;")
#     curs.execute("CREATE TABLE employers (employer_id CHAR(5) PRIMARY KEY, company_name VARCHAR(100) NOT NULL, contact_name varchar(100) NOT NULL);")
#     connect.commit()
#     info = f"INSERT INTO customers VALUES(12540, 'Power', 'Petro') returning *"
#     curs.execute(info)
#     connect.commit()
#     cur_cust = curs.fetchall()
#     curs.close()
#     connect.close()
#     return cur_cust
#
#
#
#
#
# def cont(user_host: str, user_port: str, user_database: str, user_name: str, user_password: str) -> None:
#     connect = psycopg2.connect(
#         host=f"{user_host}",
#         port=f"{user_port}",
#         user=f"{user_name}",
#         password=f"{user_password}"
#     )
#     curs = connect.cursor()
#     curs.execute("DROP TABLE employers;")
#     connect.commit()
#     curs.close()
#     connect.close()

# print(ConnectorPSQL().request_action("CREATE DATABASE new;", config()))




