# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
a = int(input())
b = int(input())
k = 0
if a > b:
    for i in range(b, a + 1):
        if i % 2 == 0 and i % 3 == 0:
            k += 1
        print(i)
    print('Числа делящиеся на 2 и 3' + '-   ' + str(k))
if b > a:
    for j in range(a, b + 1):
        if j % 2 == 0 and j % 3 == 0:
            k += 1
        print(j)
    print('Числа делящиеся на 2 и 3' + '-   ' + str(k))
