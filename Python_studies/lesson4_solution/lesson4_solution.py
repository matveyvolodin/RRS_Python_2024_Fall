# 1. Продвинутый sun.

def sum_ignore_non_numbers(items):
    """
    Возвращает сумму всех чисел в переданной последовательности
    :param items: Tuple или List
    :return:  Сумма чисел. Если чисел не передано, то возвращает 0
    """
    result = 0
    for num in items:
        if isinstance(num, (int, float)):
            result += num
    return result


print(sum_ignore_non_numbers([1, 2, 3, None]))


# 2. Треугольник.

def is_triangle(a, b, c):
    """
    Проверяет возможность существования треугольника
    :param a: Первая сторона треугольника
    :param b: Вторая сторона треугольника
    :param c: Третья сторона треугольника
    :return: Если треугольник может существовать возвращает True, Если нет, то False
    """
    return a + b > c and a + c > b and b + c > a


print(is_triangle(2,4,9))


# 3. Средние значение.

def average(*args):
    """
    Возвращает среднее арифметическое переданных чисел.

    :param args: Произвольное количество чисел (int или float).
    :return: Среднее арифметическое переданных чисел. Возвращает 0, если не переданы.
    """
    if not args:
        return 0
    return sum(args) / len(args)


print(average(1, 2, 3))


# 4. Общие строки.
fruits_1 = ["banana", "APPLE", "watermelon", "cherry"]
fruits_2 = ["Mango", "apple", "orange", "cherry"]


def common_strings(list1, list2, ignore_case=True):
    """
    Возвращает новый список с повторяющимися строками в нижнем регистре
    :param list1:    Произвольный список строк
    :param list2:    Произвольный список строк
    :param ignore_case:    Если True, то регистр игнорируется, иначе учитывается
    :return:      Новый список с повторяющимися строками из двух списков
    """
    newlist = []
    if ignore_case:
        list1 = [item.lower() for item in list1]
        list2 = [item.lower() for item in list2]
    common_elements = set(list1).intersection(set(list2))
    newlist.extend(common_elements)
    return newlist


# Вариант решения через list comprehension условие нахождение items в list1,list2
def common_strings(list1, list2, ignore_case=True):
    if ignore_case:
        list1 = [item.lower() for item in list1]
        list2 = [item.lower() for item in list2]
    return [item.lower() for item in list1 if item in list2]


print(common_strings(fruits_1, fruits_2, False))


# 1. Какое-то волнение.

text = input("Введите свой текст: ")
new_string = ""
for i in range(len(text)):
    if i % 2 == 0:
        new_string += text[i].upper()
    else:
        new_string += text[i].lower()

print(new_string)





