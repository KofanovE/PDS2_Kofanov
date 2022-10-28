# Програма обчислює суму послідовності цифр від 0 до заданого з використанням рекурсії

import random

def test_function(x):                 # Функція перевіряє, що введене число знаходиться в діапазоні від 0 до 20, або обирає рандомне число
    if not x.isdigit() or int(x) not in range(21):
        x = random.randint(0, 20)
        print(f"Digit was not right. I'm helping you: {x}")
    return int(x)

def main_function(x, sum_):          # Функція роздруковує суму послідовності чисел з використанням рекурсії
    if x > 0:
        sum_ += x
        x -= 1
        main_function(x, sum_)
    else:
        print(f"Sum = {sum_} ")

sum_ = 0
main_function(test_function(input("Enter your digit from 0 to 20: ")), sum_)





