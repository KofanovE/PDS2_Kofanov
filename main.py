import random
sum = 0
def main_function(x):
    # Функція розрахунку суми послідовності цифр заданої кількості з використанням рекурсії
    if x.isdigit() and 0 <= int(x) <= 20:
        while x >= 0:
            sum += x
            x -= 1
            main_function(x)










main_function(input("Enter your digit from 0 to 20: "))