import sys

def original_digits(s):
    try:
        if sorted(s) == list(sorted(set(s))):
            print("Даний список містить лише унікальні числа")
        else:
            print("Даний список містить повторювані числа")
    except TypeError:
        print('Список містить не тільки числа', file=sys.stderr)


a = [1, 2, 8, 1.1, 12, -12]
original_digits(a)