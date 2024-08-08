import psycopg2
import json


def connect_to_psql(user_host: str, user_port: str, user_database: str, user_name: str,
                    user_password: str) -> None:
    connect = psycopg2.connect(
        host=f"{user_host}",
        port=f"{user_port}",
        database=f"{user_database}",
        user=f"{user_name}",
        password=f"{user_password}"
    )
    curs = connect.cursor()
    curs.execute("DROP TABLE customers;")
    curs.execute("CREATE TABLE customers (customer_id CHAR(5) PRIMARY KEY, company_name VARCHAR(100) NOT NULL, contact_name varchar(100) NOT NULL);")
    connect.commit()
    info = f"INSERT INTO customers VALUES(12540, 'Power', 'Petro') returning *"
    curs.execute(info)
    connect.commit()
    cur_cust = curs.fetchall()
    curs.close()
    connect.close()
    return cur_cust


print(connect_to_psql("localhost", "5432", "vac_employers",
                "postgres", "1004"))


def cont(user_host: str, user_port: str, user_database: str, user_name: str, user_password: str) -> None:
    connect = psycopg2.connect(
        host=f"{user_host}",
        port=f"{user_port}",
        database=f"{user_database}",
        user=f"{user_name}",
        password=f"{user_password}"
    )
    curs = connect.cursor()
    curs.execute("DROP TABLE customers;")
    connect.commit()
    curs.close()
    connect.close()


print(cont("localhost", "5432", "vac_employers",
                "postgres", "1004"))
