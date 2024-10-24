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


def is_triangle(a, b, c):
    """
    Проверяет возможность существования треугольника
    :param a: Первая сторона треугольника
    :param b: Вторая сторона треугольника
    :param c: Третья сторона треугольника
    :return: Если треугольник может существовать возвращает True, Если нет, то False
    """
    return a + b > c and a + c > b and b + c > a


def average(*args):
    """
    Возвращает среднее арифметическое переданных чисел.

    :param args: Произвольное количество чисел (int или float).
    :return: Среднее арифметическое переданных чисел. Возвращает 0, если не переданы.
    """
    if not args:
        return 0
    return sum(args) / len(args)


def common_strings(list1, list2, ignore_case=True):
    """
    Возвращает новый список с повторяющимися строками в нижнем регистре
    :param list1:    Произвольный список строк
    :param list2:    Произвольный список строк
    :param ignore_case:    Если True, то регистр игнорируется, иначе учитывается
    :return:      Новый список с повторяющимися строками из двух списков
    """
    if ignore_case:
        list1 = [item.lower() for item in list1]
        list2 = [item.lower() for item in list2]
    return [item.lower() for item in list1 if item in list2]