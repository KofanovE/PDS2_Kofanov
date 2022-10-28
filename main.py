import random


def test_function(x):
    if not x.isdigit() or int(x) not in range(20):
        x = random.randint(0, 20)
        print(f"Digit was not right. I'm helping you: {x}"  )
    return int(x)

def main_function(x, sum_):
    if x > 0:
        main_function(x -= 1, sum_ += x)
    else:





        #x = int(x)
        #if x > 0:
        #    sum_ += x
        #    x -= 1
        #    main_function(str(x), sum_)
        #else:
        #    print(f"Sum = {sum_} ")


sum_ = 0
test_function(input("Enter your digit from 0 to 20: "))