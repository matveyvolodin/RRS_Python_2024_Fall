""" Повторение пройденного материала"""

# 1. Счастливый билет.

def is_lucky_ticket(ticket_id):
    """
     Функция проверяет: является ли номер билета счастливым
    :param ticket_id: Прозвольный шестизначный номер билета
    :type ticket_id: int
    :return: True, если номер счастливый, False, если нет
    :rtype: bool
    """
    if type(ticket_id) is not int:
        raise TypeError (f"Некорректный тип данных: {type(ticket_id).__name__}, ожидается int")
    elif len(str(ticket_id)) != 6:
        raise ValueError (f"Количество цифр в номере билета должно равняться шести, введено: {(len(str(ticket_id)))}")
    first_three = sum(int(i) for i in str(ticket_id)[:3])
    last_three = sum(int(i) for i in str(ticket_id)[3:])
    return first_three == last_three


print(is_lucky_ticket(1111111))

# 2. Числа Армстронга.

result = []

for i in range(100, 1001, 1):
    cube_sum = sum(int(digit)**3 for digit in str(i))
    if cube_sum == i:
        result.append(i)
print(result)


# 3. Цензор.

def censor_print(string):
    """
    Функция заменяет слова из string на "***", если они включены в ban_dict и выводит измененную string в консоль
    :param string: Произвольный текст, вводится пользователем
    :type string: str
    :return: Редактированная string
    :rtype: str
    """
    ban_dict = ["Мир", "Демократия"]
    for ban_word in ban_dict:
        string = string.replace(ban_word, "***")
    return string

print(censor_print("Мир, труд, май, и Демократия"))


# 4.* D...

flashcards = {
    "city": {
        "taxi": "такси",
        "employer": "работодатель",
        "staff": "персонал"
    },
    "kitchen": {
        "plate": "тарелка",
        "fork": "вилка",
        "pot": "кастрюля"
    },
    "sport": {
        "barbell": "штанга",
        "dumbbell": "гантеля",
        "bicycle": "велосипед"
    }
}

while True:
    selected_topik = input(f"Привет! Выбери сегодняшнюю тему для изучения: {', '.join(flashcards.keys())}... или введи выйти: ")
    if selected_topik == "выйти":
        print("Но ты приходи еще!")
        break
    elif selected_topik in flashcards:
        score = 0
        total_questions = len(flashcards[selected_topik])
        for word, translation in flashcards[selected_topik].items():
            answer = input(f" Введите перевод слова {word}: ").lower()
            if answer == translation:
                print("Верно")
                score += 1
            else:
                print(f"Неверно, правильный перевод слова: {translation}")
        print(f"Ты ответил правильно на {score} вопросов из {total_questions}")



