sum = 0
while(True):
    f = False
    x = input("Введите цифру, или stop/end для выхода из цикла:")
    if x == "stop" or x == "end":
        print("Сумма всех ранее ввёденных значений:", sum)
        break
    else:
        for i in x:
            if i == ".":
                continue
            elif i.isdigit() == False:
                print("Неверный ввод!")
                f = True
                continue
        if f == False:
            sum += float(x)
        else:
            f == False