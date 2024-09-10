# 1 Четное или нечетное
n = input("Enter your number: ")
if int(n) % 2:
    print("Odd")
else:
    print("Even")


# 2 Какой сегодня день?

day = input("Выбери один из дней недели: ")
if day == "суббота" or day == "воскресенье":
    print("Сегодня выходной!")
elif day == "среда":
    print("Мне сегодня к стоматологу в 15:30")
else:
    print("Сегодня обычный день")


# 3 Эхо

n = int(input("Введи число"))
text = input("Введи строку")
while n > 0:
    n -= 1
    print(text)


# 4 Сколько гласных букв?
chars = ""
message = input("Введи сообщение")
for c in message:
    if c in "йуеыаэяиюо":
        chars += c
print(len(chars))


counter = 0
message = input("Введи сообщение")
for c in message:
    if c in "йуеыаэяиюо":
        counter += 1
print(counter)


# 5 Сумма чисел
nlist = []
while True:
    num = int(input("Введи число"))
    nlist.append(num)
    if num < 0:
        break
print(sum(nlist))


counter = 0
while True:
    num = int(input("Введи число: "))
    counter += num
    if num < 0:
        break
print(counter)
