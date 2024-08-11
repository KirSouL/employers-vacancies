import os


def path_to_data():
    """
    Функция создающая путь до директории базы данных.
    :return: возвращает путь до директории базы данных.
    """
    path_to_save = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))

    return path_to_save


def path_to_src():
    """
    Функция создающая путь до директории ресурсов.
    :return: возвращает путь до директории ресурсов.
    """
    path_to_save = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))

    return path_to_save


def path_to_utils():
    """
       Функция создающая путь до директории утилит.
       :return: возвращает путь до директории утилит.
       """
    path_to_save = os.path.abspath(os.path.join(os.path.dirname(__file__), "utils"))

    return path_to_save
