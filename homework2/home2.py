k = 0
while k != 1:
    print("Введите два числа")
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    if (a.isdigit() and b.isdigit()):
        print("Сумма введенных чисел равна:", int(a) + int(b))
    else:
        print("Программа была остановлена по причине вашей глупости. Автор не даст вам продолжить.")
        break
