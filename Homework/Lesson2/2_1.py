# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр. Без работы с методами строк.

num = float(input("Введите число"))
DigitSum = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    DigitSum += num % 10
    num //= 10

print(int(DigitSum))