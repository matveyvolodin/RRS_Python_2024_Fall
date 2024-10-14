# """Обработка ошибок и исключений"""
#
#
# # 1. Регистрация.
# class RegistrationError(Exception):
#     pass
#
#
# def registration(username, password):
#     if not isinstance(username, str) or 4 > len(username) > 15 or username.isdigit():
#         raise RegistrationError("Некорректный username")
#     if not isinstance(password, str) or 8 > len(password) > 48 or password.isalnum():
#         raise RegistrationError("Некорректный password")
#     return True
#
#
# # print(registration("Avasdasd ", "1233455#A4"))
#
# # 2. Регистрация (часть 2).
#
# while True:
#     new_username = input("Введите новый username: ")
#     new_password = input("Введите новый password: ")
#     try:
#         registration(new_username, new_password)
#         print("Успешно")
#         break
#     except RegistrationError as e:
#         print(f"Ошибка операции: {e}")


# 3. Дорогой дневник.
while True:
    string = input("Введите одну из следующих команд: 'прочитать', 'записать', 'выйти': ")
    if string == "записать":
        while True:
            with open("journal.txt", "a", encoding="utf-8") as file:
                message = input("Что записать в журнал?: ")
                file.write("\n" + message)
                if message == "выйти":
                    break
    elif string == "прочитать":
        with open("journal.txt", "r", encoding="utf-8") as file:
            print(file.read())
    elif string == "выйти":
        print("Еще увидимся")
        break




