# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет
number = int(input())
answer = "YES"
while number // 10:
    sample_right = number % 10
    number = number // 10
    sample_left = number % 10
    if sample_right <= sample_left:
        answer = "NO"
        break
print(answer)
