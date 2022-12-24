"""Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11"""

number = input("Введите вещественное число: ")

def sum_of_digits(number):
    sum = 0
    for i in str(number):
        if i != "," and i != ".":
            sum += int(i)
    return sum

print(sum_of_digits(number))




