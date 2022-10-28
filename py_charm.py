# Програма підраховування суми чисел в задоному рядку з найменшою кількістю коду
import random
digit = (input("Enter your number from 0 to 10: "))
right_digit = lambda  digit  : (digit if digit.isdigit() and 0 <= int(digit) <= 20 else random.randint(0, 20))
print(f"The sum of line with max {right_digit(digit)} = {sum([i for i in range(1, int(right_digit(digit))+1)])}")
