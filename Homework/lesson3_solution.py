# 1. Особые числа.

numbers = []

for i in range(101):
    if i % 2 == 0 and i % 3 == 0:
        numbers.append(i)
print(numbers)


numbers = [i for i in range(101) if i % 2 == 0 and i % 3 ==0]
print(numbers)


# 2. Фильтр.

items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# Решение при помощи list comprehension
numbers = [i for i in items if isinstance(i, (int, float))]
print(sum(numbers))


# 3. История сообщений.

messages = []
while True:
    message = input("Введи свое сообщение: ")
    messages.append(message)
    if len(messages) > 5:
        messages.remove(messages[0])
    if message == "пока":
        print(f"Ну ладно, пока! {messages}")
        break

# 4. Без дубликатов.

# Решение при помощи множества
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
num_set = set(numbers)
sorted_list = sorted(num_set)
print(sorted_list)

# Решение при помощи цикла
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(sorted(new_list))

# Дополнительное задание.

# 1. Магазин.
products = {
    "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk": {"quantity": 12, "price": 90},
    "bread": {"quantity": 30, "price": 40}
}
for data in products.values():
    data["price"] *= 1.2

del (products["milk"])
products["salt"] = {"quantity": 7, "price": 12}

total_price = 0
for data in products.values():
    total_price += data["quantity"] * data["price"]
print(total_price)


d=[1, 6, 9]

def a(d):
    for i in range(d[0], d[-1]+1):
        if not i in d:
            d.append(i)
            d.sort()
    return d

print(a(d))