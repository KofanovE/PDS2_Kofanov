from _13_2_heap_sort import average

def main():
    num = 3
    time_average = average(selection_sort, num)
    print("_______________________________")
    print(f"Average time Selection Sort method for this task: {round(sum(time_average) / len(time_average), 4)} sec")


def selection_sort(list_):
    list_result = []
    num = len(list_)
    count = 0
    while True:
        for i in range(len(list_)):
            if list_[i] < list_[0]:
                list_[i], list_[0] = list_[0], list_[i]
                count += 1
        list_result.append(list_.pop(0))
        if len(list_result) == num:
            break
    # print(list_result)
    return count



if __name__ == "__main__":
    main()
