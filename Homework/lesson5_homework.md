### ООП, классы
### 1. Прямоугольник.

- Создайте класс Rectangle, который принимает ширину и высоту
прямоугольника при создании и должен иметь соответствующие атрибуты
width и height (целые числа).
- Создайте метод area(), который возвращает площадь прямоугольника.
- Создайте метод perimeter(), который возвращает периметр
прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12

### 2. Автомобиль.

- Создайте класс Car, который принимает марку автомобиля (make) в виде
строки и максимально возможную скорость (max_speed) в виде целого
числа при создании. Также при инициализации (в теле __init__) экземпляра
Car должен быть автоматически создан атрибут speed, равный 0 (текущая
скорость автомобиля).
- Создайте метод display_speed(), который выводит в консоль текущую
скорость автомобиля.
- Создайте метод accelerate(), который увеличивает скорость автомобиля на
10, при этом скорость автомобиля не должна превышать max_speed, если
вызывается accelerate() при максимальной скорости, то скорость не
должна увеличиваться.
- Создайте метод brake(), который уменьшает скорость автомобиля на 10,
при этом скорость автомобиля не может быть меньше 0. Если вызывается
метод brake() при скорости равной 0, то скорость не должна уменьшаться.
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()

my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 30

### 3. Интернет-банк.

- Создайте класс BankAccount, который принимает имя владельца (name) в
виде строки и текущее состояние счета (balance) в виде целого числа. Оба
этих атрибута должны быть _защищенным.
- Создайте метод deposit(), который принимает 1 аргумент (если не считать
self, конечно) amount (целое число). Метод должен увеличить текущий
баланс аккаунта на amount.
- Создайте метод withdraw(), который принимает 1 аргумент amount (целое
число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
денег на счету недостаточно, то метод выводит на экран “Недостаточно
средств!”.
- Создайте метод get_balance(), который возвращает текущее значение
баланса аккаунта.
Пример:
account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500

### 4. Овердрафт.

- Создайте класс OverdraftAccount, унаследованный от вашего класса
BankAccount из предыдущей задачи.
- Переопределите существующий метод withdraw(), но теперь, если баланс
аккаунта меньше или равен 0, то это не выводит на экран сообщение
“Недостаточно средств!”, а уменьшает баланс в минус.
Пример:
jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)

jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300

### Повторение прошлого материала.

Ответьте на следующие вопросы:
1. Что такое and, or и not? Приведите пример их использования.
2. Что такое цикл? Чем отличается for от while?
3. Как нельзя именовать переменную? Почему я не могу назвать переменную
max или min?
4. Что такое функция? Зачем она нужна?