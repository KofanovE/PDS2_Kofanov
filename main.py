import random


def main_function(x, sum_):
    # Функція розрахунку суми послідовності цифр заданої кількості з використанням рекурсії
    if x.isdigit() and 0 <= int(x) <= 20:
        x = int(x)
        while x > 0:
            sum_ += x
            x -= 1
            main_function(str(x), sum_)
        print(f"Sum = {sum_} ")









sum_ = 0
main_function(input("Enter your digit from 0 to 20: "), sum_)