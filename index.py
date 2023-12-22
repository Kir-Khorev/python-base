# === Типы данных ===

# Числовые типы данных
integer_number = 42
float_number = 3.14

# Строковый тип данных
my_name = "John"

# Логический тип данных
is_adult = True

# Список
my_list = [1, 2, 3, "apple", True]

# Кортеж (упорядоченные неизменяемые последовательности)
my_tuple = (1, 2, "banana", False)

# Множество  (неупорядоченные наборы уникальных элементов)
my_set = {1, 2, 3, 3, 4}

# Словарь
my_dict = {"name": "Alice", "age": 28, "city": "Wonderland"}

# Вывод значений в консоль
print("Integer Number:", integer_number)
print("Float Number:", float_number)
print("My Name:", my_name)
print("Is Adult:", is_adult)
print("My List:", my_list)
print("My Tuple:", my_tuple)
print("My Set:", my_set)
print("My Dictionary:", my_dict)


# Пример объявления переменных разных типов
age = 25         # Целочисленный тип данных
height = 1.75    # Тип данных с плавающей точкой
name = "John"    # Строковый тип данных
is_adult = True  # Логический тип данных

# Вывод значений переменных
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Adult:", is_adult)

# Арифметические операторы
result_add = 5 + 3
result_sub = 10 - 4
result_mul = 6 * 2
result_div = 8 / 4

# Логические операторы
is_true = True
is_false = False

logical_and = is_true and is_false
logical_or = is_true or is_false
logical_not = not is_true

# ======================== Операторы сравнения
greater_than = 10 > 5
less_than = 3 < 7
equal_to = 4 == 4
not_equal_to = 6 != 3

# Вывод результатов
print("Arithmetic Operators:")
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)

print("\nLogical Operators:")
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)

print("\nComparison Operators:")
print("Greater Than:", greater_than)
print("Less Than:", less_than)
print("Equal To:", equal_to)
print("Not Equal To:", not_equal_to)

# ========== Пример условного оператора
number = 15

if number > 10:
    print("Число больше 10")
elif number == 10:
    print("Число равно 10")
else:
    print("Число меньше 10")


# ================= Циклы =============
    # Пример использования цикла for
for number in range(1, 4):
    # Цикл будет выполняться три раза: с 1 по 3 (не включительно)
    print("Number:", number)

# Пример использования цикла while
counter = 0

while counter < 3:
    # Цикл будет выполняться, пока счетчик меньше 3
    print("Counter:", counter)
    counter += 1  # Увеличиваем счетчик на 1 на каждой итерации

# Пример ввода данных с клавиатуры
# user_name = input("Введите ваше имя: ")
# print("Привет, " + user_name + "!")

# Пример вывода данных
age = 25
height = 1.75

# Вывод с использованием форматирования строк
print("Мой возраст: {}, а мой рост: {:.2f}".format(age, height))

# Вывод с использованием f-строк (доступно в Python 3.6 и выше)
print(f"Мой возраст: {age}, а мой рост: {height:.2f}")


# ========================= Функции ===================

# Пример определения функции
# Пример функции с параметрами и возвращаемым значением
def add_numbers(a, b):
    """
    Функция сложения двух чисел.
    
    Parameters:
        a (int): Первое число.
        b (int): Второе число.
    
    Returns:
        int: Сумма a и b.
    """
    result = a + b
    return result

# Вызываем функцию с конкретными аргументами
sum_result = add_numbers(3, 5)
print("Сумма чисел:", sum_result)

# Пример лямбда-функции (анонимной функции)
multiply = lambda x, y: x * y

# Вызов функции сложения чисел
sum_result = add_numbers(310, 5)
print("Сумма чисел:", sum_result)

# Вызов лямбда-функции умножения
product = multiply(2, 4)
print("Произведение чисел:", product)


# =============== Работа с файлами: ====================

# Пример открытия файла в режиме записи ('w')
file_path = "index.txt"

# Открытие файла для записи (если файла нет, он будет создан)
with open(file_path, "w") as file:
    file.write("Привет, мир!\nЭто файловая работа в Python.")
    
# Файл автоматически закроется после блока кода с использованием ключевого слова `with`

# Пример чтения данных из файла
with open(file_path, "r") as file:
    content = file.read()
    print(content)


# ============== Обработка исключений ===============
    
    # Пример конструкции try/except для обработки ошибок
try:
    # Код, который может вызвать исключение
    num1 = int(input("Введите число: "))
    num2 = int(input("Введите еще одно число: "))
    
    result = num1 / num2
    print("Результат деления:", result)

except ZeroDivisionError:
    # Обработка исключения деления на ноль
    print("Ошибка: Деление на ноль!")

except ValueError:
    # Обработка исключения ввода некорректного значения
    print("Ошибка: Введите корректное число!")

except Exception as e:
    # Обработка других исключений
    print(f"Произошла ошибка: {e}")

else:
    # Блок выполняется, если в блоке try не было исключений
    print("Деление выполнено успешно!")

finally:
    # Блок выполняется всегда, независимо от того, было ли исключение или нет
    print("Блок finally выполнен.")

# ====================== OOP =====================
    
    # Пример создания класса
class Dog:
    # Атрибут класса
    species = "Canis familiaris"
    
    # Метод инициализации (конструктор)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Метод класса
    def bark(self):
        print(f"{self.name} лает!")

# Создание объекта (экземпляра) класса
my_dog = Dog(name="Барон", age=3)

# Доступ к атрибутам объекта
print(f"{my_dog.name} - {my_dog.age} года")

# Вызов метода объекта
my_dog.bark()

# Пример использования наследования, инкапсуляции и полиморфизма

# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Метод speak должен быть определен в подклассе")

# Подкласс с наследованием
class Dog(Animal):
    def speak(self):
        return f"{self.name} лает!"

# Еще один подкласс с наследованием
class Cat(Animal):
    def speak(self):
        return f"{self.name} мяукает!"

# Создание объектов разных классов
my_dog = Dog(name="Барон")
my_cat = Cat(name="Мурка")

# Использование полиморфизма
animals = [my_dog, my_cat]

for animal in animals:
    print(animal.speak())


# ======================= Модули ==================

# Пример импортирования модуля math
import math

# Использование функций из модуля
print("Квадратный корень из 16:", math.sqrt(16))
print("Значение числа pi:", math.pi)

# Импорт собственного модуля
import my_module

# Использование функции из модуля
message = my_module.greet("Ozzie")
print(message)

# Импорт собственного пакета и модуля
from my_package import my_submodule

# Использование функции из подмодуля пакета
result = my_submodule.multiply(3, 4)
print("Результат умножения из подмодуля:", result)


# ================ Requests ================

import requests

# Пример GET-запроса
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Проверка успешности запроса
if response.status_code == 200:
    # Вывод данных из ответа
    data = response.json()
    print("Заголовок задачи:", data['title'])
else:
    print("Ошибка при выполнении запроса:", response.status_code)