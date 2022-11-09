
def name_month():
    dict_names = {'1': 'January',
                  '2': 'Fabruary',
                  '3': 'March',
                  '4': 'April',
                  '5': 'May',
                  '6': 'June',
                  '7': 'July',
                  '8': 'August',
                  '9': 'September',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December'}
    while True:
        nomber_month = input("Input number of month: ")
        try:
            if not nomber_month.isdigit():
                raise ValueError()
            print(dict_names[nomber_month])
            break
        except KeyError:
            print("Input right number of month from 1 to 12!\n")
            continue
        except ValueError:
            print("It isnt number of month!\n")
            continue

name_month()



