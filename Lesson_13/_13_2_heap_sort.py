import time
from _13_1_random_lists import _int_list
# Не вдалося нормально реалізувати пірамідальне сортування
# Дане сортування виявилося в 15 раз повільнішим і на 30% більше інтераций, ніж у вибіркового сортування


def main():
    num = 3                               # Задана кількість сортувань
    time_average = average(heap_sort, num) # Список таймінгу інтерацій сортування
    print("_______________________________")
    print(f"Average time Heap Sort method for this task: {round(sum(time_average) / len(time_average), 4)} sec")


def average(sort_metod, num):
    # Функція приймає метод сортування та кількість інтерацій,
    # використовуючи функцію  рандомного списку з _13_1_random_lists, проводиться задана кількість інтерацій з возвратом часу
    time_average = []
    for i in range(1, num+1):
        list_ = _int_list()
        time_0 = time.time()
        inter = sort_metod(list_)
        time_average.append(time.time() - time_0)
        print(f"{i}. Interations: {inter}, Time: {time_average[-1]}")
    return time_average


def list_to_dict(list_):
    # функція приводить рандомний список до словника, де ключ - рівень піраміди,
    # змінні- вузли піраміди на відповідному рівні
    # типу {1: [1], 2: [2, 3], 3: [4, 5, 6, 7]}
    dict_ = {}
    start = 0
    stop = 1
    sum = 0
    i = 1
    while sum < len(list_):
        dict_[i] = list_[start: stop]
        start = stop
        stop = start * 2 +1
        sum += len(dict_[i])
        i += 1
    return dict_


def heap_sort(list_):
    dict_ = list_to_dict(list_)
    result_list = []
    count = 0
    while True:         # Інтерації формування відсортованого списку
        while True:     # Інтерації сортування піраміди
            flag = True    # Флаг відсутності інтерацій
            try:
                for key in dict_: # Для кожного рівня піраміди
                    for i in range(len(dict_[key])): # Для кожного номеру вузла даного рівня піраміди
                        value = dict_[key]           # Список вузлів даного рівня
                        if key == len(dict_) or i*2 > len(dict_[key+1]):               # Якщо це отсанній рівень або в наступному рівні нема даного дочірнього вузла
                            raise IndexError()                                         # Визов IndexError
                        if value[i] < dict_[key+1][i*2]:                                # Якщо даний вузол менше за перший дочірній
                            value[i], dict_[key+1][i*2] = dict_[key+1][i*2], value[i] # Батьківський і дочірній вузли міняються місцями
                            count += 1                                                 # Лічильник інтерацій інкрементується
                            flag = False                                               # Флаг: інтерація відбулася
                        if i*2+1 > len(dict_[key+1]):                                                # якщо в наступному рівні відсутній даний дочірній вузол
                            raise IndexError()                                                       # Визов IndexError
                        if value[i] < dict_[key+1][i*2+1]:                                           # Якщо даний вузол менше за другий дочірній
                            value[i], dict_[key + 1][i * 2 +1] = dict_[key + 1][i * 2 + 1], value[i] # Перестановка вузлів
                            count += 1                                                               # Лічильник інтерацій інкрементується
                            flag = False                                                              # Флаг: інтерація відбулася

            except IndexError:        # Якщо спрацювала обробка IndexError
                if flag:              # Якщо інтерацій не було - вихід із циклу обходу піраміди
                    break
                else:
                    continue

        result_list.append(dict_[1].pop())          # З відсортованої піраміди корень (найбільше число) вноситься в відсортований список
        dict_[1].append(dict_[len(dict_)].pop())    # Корень заміняється на видалений кінцевий елемент останнього рівня (піраміда зменшується знизу)
        if dict_[len(dict_)] == []:                 # Якщо останній рівень піраміди не має вузлів - рівень видаляється
            dict_.pop(len(dict_))
        if len(dict_) == 1:                        # Якщо в піраміді остався тільки корневий рівень - корень (найменше число, що лишилося) ставиться в кінець відсортованого списку
            result_list.append(dict_[1].pop())
            break

    # print(result_list[::-1])
    return count                                  # Повертається кількість інтерацій



if __name__ == "__main__":
    main()