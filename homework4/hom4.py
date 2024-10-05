print("Введите два числа и программа выведет целые числа в их диапазоне, первое число должно быть меньше второго.")
k = 0
a = input("Введите первое число ")
for j in a:
    if (j == '.'):
        continue
    elif j.isdigit() == False:
        print("Проверьте, что ввели цифру, а не букву")
        break
b = input("Введите второе число ")
for u in b:
    if (u == '.'):
        continue
    elif u.isdigit() == False:
        print("Проверьте, что ввели цифру, а не букву")
        break
if (a < b):
    for i in range(int(float(a)+1), int(float(b)+1), 1):
            print(i)
            k+=1
    if (k == 0):
        print("Целых чисел нет")
else:
    print("Читайте условие внимательно")