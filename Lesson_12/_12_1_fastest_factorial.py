import concurrent.futures
import os
from time import time
from multiprocessing import Pool

global result
result = 1
n = 300    # Базове число пошуку факторіалу
l = [i for i in range(1, n + 1)]
cpu = os.cpu_count()


def main():
    # Словник: ключі - методи, значення - середнє значення часу з 10ти спроб по кожному методу.
    result_dict = {"MultiprocessingMetod": mean([MMP_factorial() for i in range(10)]),
                   "ThreadPollExecutor": mean([TPE_factorial() for i in range(10)]),
                   "ProcessPollExecutor": mean([PPE_factorial() for i in range(10)])
                  }
    # Середнє значення з 10ти спроб однопотоковим методом
    SP_time = mean([SP_factorial() for i in range(10)])
    # Список приймає єдине значення - ключ найшвидшого метода в словнику result_dict
    best_method = [key for key in result_dict if result_dict[key] == min(result_dict.values())]

    print(f"Для даної задачі найоптимальніший багатопотоковий метод: {best_method[0]}")
    print(f"{best_method[0]} вирішує дану задачу в сердньому за {result_dict[best_method[0]]} c")
    print(f"Однопотоковий метод вирішує дане завдання в середньому  за {SP_time} c")


#MultiprocessingMetod
def MMP_factorial():
    global result
    result = 1
    time_MMP = time()
    with Pool(cpu) as p:
        x = list(p.map(factorial, l))[-1]
        # print(x[-1])
        #print(time() - time_MMP)
        return time() - time_MMP


# ThreadPollExecutor
def TPE_factorial():
    time_TPE = time()
    global result
    result = 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=cpu) as executor:
        executor.submit(factorial, 1)
        list_factorial = list(executor.map(factorial, l))
        # print(list_factorial[-1])
        # print(time() - time_TPE)
        return time() - time_TPE


# ProcessPollExecutor
def PPE_factorial():
    time_PPE = time()
    global result
    result = 1
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu) as executor:
        list_factorial = list(executor.map(factorial, l))
        # print(list_factorial[-1])
        # print(time() - time_PPE)
        return time() - time_PPE

# Однопотоковий метод
def SP_factorial():
    time_SP = time()
    global result
    result = 1
    for i in l:
        result_ = factorial(i)
    # print(result_)
    # print(time() - time_SP)
    return time() - time_SP


# Функція пошуку факторіалу
def factorial(x):
    global result
    result = result * x
    return result

# Функція пошуку середнього значення в списку
def mean(list_):
    mean_ = sum(list_)/len(list_)
    return mean_


if __name__ == "__main__":
    main()