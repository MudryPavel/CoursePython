number=int(input("Введите день недели:"))
while (number>7) or (number<1):
    print("Некорректный ввод ")
    number=int(input("Введите день недели:"))
if (number == 6) or (number == 7):
    print("Сегодня выходной")
else:
    print("Сегодня будний день")
