import random
from random_words import RandomWords


def main():
    print(_int_list())
    print(_float_list())
    print(_str_list())


def _int_list():
    int_list = [random.randint(0, 1000) for i in range(5000)]
    return int_list


def _float_list():
    float_list = [round(random.uniform(0.1, 100.0), 1) for i in range(5000)]
    return float_list


def _str_list():
    w = RandomWords()
    str_list = [w.random_word() for i in range(5000)]
    return str_list



if __name__ == "__main__":
    main()