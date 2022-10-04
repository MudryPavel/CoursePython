# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num = int(input())
NumberSum = 0
NumberList = []

for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i)
    NumberList.append(result)
    NumberSum += result

print(NumberList)
print(NumberSum)