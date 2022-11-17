# Задать список произвольных чисел, кол-во задает пользователь.
# Напишите программу, определяющую присутствует ли в заданном списке число, полученное от пользователя.

from random import sample
def numCheck(num, size):
    if size < 0:
        return "Error"
    list1 = sample(range(1, size*2), size)
    print(list1)
    if num in list1:
        return "Yes"
    return "No"
print(numCheck(int(input()),int(input())))