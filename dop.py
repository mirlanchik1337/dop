# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numbers if x % 2 == 0] #пример list сomplehenntion
#
# numbers = [1, 2, 3, 4, 5]
# squares_dict = {x: x**2 for x in numbers} #пример list сomplehenntion
#

#
# import turtle
#
# screen = turtle.Screen()
# screen.bgcolor('black')
#
# t = turtle.Turtle()
# t.speed(0)
#
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#
# for i in range(300):
#     t.color(colors[i % 6])
#     t.forward(i * 2)
#     t.left(59)
#
# turtle.done() # прикольный код

#add = lambda x, y: x + y
# print(add(2, 3))

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(name, age)
#
# s = "Hello, world!"
# print(s[::-1]) # cрезы
#
#
# s = "Hello, world!"
# print(s[:5])       # вывести первые 5 символов
# print(s[7:])       # вывести все символы, начиная с 7-го
# print(s[::2])      # вывести каждый второй символ
# print(s[::-1])     # вывести строку задом наперед
# print(s[-6:-1])    # вывести подстроку "world"
# print(s[-1::-1])   # вывести строку задом наперед с последним символом
# #
#
#
# text = "Hello, my name is John. What is your name?"
# words = text.split()  # разбить текст на слова
#
# counts = {}  # словарь для хранения числа вхождений каждого слова
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# for word, count in counts.items():
#     print(f"{word}: {count}") # cортировка чисел

#


# def is_prime(n): определение сколько чисел до заданного числа есть
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# n = int(input("Введите число: "))
#
# for i in range(2, n+1):
#     if is_prime(i):
# #         print(i)
#
# while 1:
#     n = int(input("Введите число: "))
# 
#     factorial = 1
#     for i in range(2, n+1):
#         factorial *= i
#
#     print(f"Факториал числа {n}: {factorial}")
#

#
# from datetime import datetime, timedelta
#
# days = 30
#
# today = datetime.today()
# future_date = today + timedelta(days=days)
#
# print(f"Через {days} дней будет {future_date:%Y-%m-%d}")
