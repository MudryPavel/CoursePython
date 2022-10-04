# 2. Напишите программу, которая принимает на вход число N 
#    и выдает набор произведений чисел от 1 до N в виде списка. 

num = int(input())
DigitSum = 1

for i in range(num):
    DigitSum *= i + 1
    print(DigitSum, end=", ")