import random

def main_function(x, sum_):
    # Функція розрахунку суми послідовності цифр заданої кількості з використанням рекурсії
    if x.isdigit() and 0 <= int(x) <= 20:
        x = int(x)
        if x > 0:
            sum_ += x
            x -= 1
            main_function(str(x), sum_)
        else:
            print(f"Sum = {sum_} ")
    else:
        x = random.randint(0, 20)
        print(f"Your digit from 0 to 20 isn't right! I'm helping you: {x}")
        main_function(str(x), sum_)


sum_ = 0
main_function(input("Enter your digit from 0 to 20: "), sum_)