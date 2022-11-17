# Задайте список, состоящий из произвольных слов, количество задает пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке либо сообщит, что ее нет.
from random import choices
def wordlist(size, word):
    new_list =[]
    for i in range(size):
        a=choices(word,k=3)
        new_list.append(''.join(a))
    return new_list
list2=(wordlist(125, "abc"))
print(list2)
def wordCheck(list1, key, searchIndex):
    size=len(list1)
    resList =[]
    for i, word in enumerate(list1):
        if word==key:
            resList.append(i)
    print(resList)
    print(resList[searchIndex])
    return resList[searchIndex]
wordCheck(list2, "abc", 1)
