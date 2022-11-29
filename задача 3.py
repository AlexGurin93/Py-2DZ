# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
price = input("Введите сумму:")
price = int(price)
price1 = price % 25
price2 = price % 10
price3 = price % 3
price4 = price3 // 1
price5 = price2 // 3
price6 = price1 // 10
price7 = price // 25
print(price4, "- по 1р")
print(price5, "- по 3р")
print(price6, "- по 10р")
print(price7, "- по 25р")
