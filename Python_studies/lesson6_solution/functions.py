import requests
import pickle
import os

base_url = "https://restful-booker.herokuapp.com/booking"
create_token_url = "https://restful-booker.herokuapp.com/auth"


def get_booking_by_id(booking_id):
    """
    Посылает GET запрос и выводит информацию бронирования по ID
    :param booking_id: ID зарегистрированного бронирования
    :return: Response, ответ с объектом с сервера
    """
    return requests.get(base_url + f"/{booking_id}")


def get_all_bookings():
    """
    Посылает GET запрос и выводит информацию обо всех бронированиях
    :return: Response, объект с ответом сервиса
    """
    return requests.get(base_url)


def create_booking(data):
    """
    Посылает POST запрос на создание букинга
    :param data: dict, содержащий информацию о бронировании
    :return: Response, объект с ответом сервиса
    """
    return requests.post(base_url, json=data)


def create_token(username, password):
    """
    Создает токен авторизации и возвращает его
    :param username: str, Имя пользователя для авторизации
    :param password:  str, Пароль для авторизаци
    :return: токен аутентификации
    """
    token_info = {
        "username": f"{username}",
        "password": f"{password}"
    }
    response = requests.post(create_token_url, json=token_info)
    token_info = response.json()
    return token_info.get("token")


def patch_booking(new_data, headers, booking_id):
    """
    Частично обновляет созданный букинг
    :param new_data: dict, Новые данные которые должны быть внесены в букинг
    :param headers: dict, заголовки для передачи с запросом
    :param booking_id: int, ID бронирования
    :return: Response, объект с ответом сервера
    """
    return requests.patch(base_url + f"/{booking_id}", json=new_data, headers=headers)


def delete_booking_by_id(booking_id, headers):
    """
    Удаляет созданный букинг по его id
    :param booking_id: int, ID созданного букинга
    :param headers: dict, заголовки для передачи с запросом
    :return: Response, объект с ответом сервера
    """
    return requests.delete(base_url + f"/{booking_id}", headers=headers)


# 1. Калькулятор.
class Calculator:
    def __init__(self):
        self.history_file = "calc_history.pkl"
        self.history = self.load_history()

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        self.save_history()
        return result

    def mul(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return a * b

    def div(self,a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Деление на ноль невозможно")
            return "Деление на ноль невозможно"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return a / b

    def show_operations(self):
        """
        Отображает историю операций калькулятора
        :return: list, история операций
        """
        return self.history

    def clear_history(self):
        """
        Отчищает историю операций калькулятора
        :return: list, пустой список
        """
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            self.history = []
            print("История операций успешно отчищена")
        else:
            print("История операций пуста")

    def save_history(self):
        """
        Сохраняет историю вычислений в файл
        """
        with open(self.history_file, "wb") as f:
            pickle.dump(self.history, f)

    def load_history(self):
        """
        Загружает историю вычислений из файла
        :return: Если файл существует, возвращает файл со списком вычислений, если не существует,
        возвращает пустой список.
        """
        if os.path.exists(self.history_file):
            with open(self.history_file, "rb") as f:
                return pickle.load(f)
        return []