import os


def path_to_data():
    """
    Функция создающая путь до директории базы данных.
    :return: возвращает путь до директори базы данных.
    """
    path_to_save = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))

    return path_to_save
