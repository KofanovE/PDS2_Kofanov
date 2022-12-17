# Напишіть клас для роботи з матрицями. Клас повинен створювати об'єкт матриць з вкладених списків,
# виводити матриці на друк, виконувати операції додавання, віднімання, множення на число, множення на матрицю,
# транспонування. Передбачте можливість приведення матриці для операцій додавання і віднимання, та обробку виключних
# ситуацій для операції множення матриці на матрицю.

class MatrixClass:

    def __init__(self, obj):
        try:
            for i in range(len(obj)):
                if type(obj) == list and type(obj[i]) == list: #chek, that entered object is list of lists
                    if obj == [[]]:
                        self.matrix = [[]]
                        return None
                    for j in obj[i]:
                        if not (type(j) == int or type(j) == float): #chek, that lists are including int or float digits
                            print("all elements of matrix must be digits")
                            self.matrix = [[]]
                            return None
                    self.matrix = obj #else, matrix is entered list of lists
                else: # else not list of lists, created matrix is empty
                    print("obj isn't list of lists")
                    self.matrix = [[]]
                    return None
        except TypeError: # if not interate objects, matrix is empty
            print("obj isn't list of lists")
            self.matrix = [[]]

    def __str__(self):
        return self.matrix


    def __matching(self, obj_2): # method om matching two matrix
        lines = len(self.matrix) - len(obj_2.matrix) # matching lines
        if lines > 0:
            for i in range(lines):
                obj_2.matrix.append([])
        elif lines < 0:
            for i in range(lines * (-1)):
                self.matrix.append([])

        for i in range(len(self.matrix)): # matching columns
            columns = len(self.matrix[i]) - len(obj_2.matrix[i])
            if columns > 0:
                for j in range(columns):
                    obj_2.matrix[i].append(0)
            elif columns < 0:
                for j in range(columns * (-1)):
                    self.matrix[i].append(0)
        num_members = 0
        for i in range(len(self.matrix)):
            if num_members < len(self.matrix[i]) or num_members < len(obj_2.matrix[i]):
                if len(self.matrix[i]) >= len(obj_2.matrix[i]):
                    num_members = len(self.matrix[i])
                elif len(self.matrix[i]) < len(obj_2.matrix[i]):
                    num_members = len(obj_2.matrix[i])
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) < num_members:
                self.matrix[i].append(0)
            if len(obj_2.matrix[i]) < num_members:
                obj_2.matrix[i].append(0)


    def __add_digit(self, obj_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + obj_2)
        self.matrix = result



    def __sub_digit(self, obj_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - obj_2)
        self.matrix = result


    def __mul_digit(self, obj_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] * obj_2)
        self.matrix = result


    def __add_matrix(self, obj_2):
        self.__matching(obj_2)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + obj_2.matrix[i][j])
        self.matrix = result


    def __sub_matrix(self, obj_2):
        self.__matching(obj_2)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - obj_2.matrix[i][j])
        self.matrix = result

    def __mul_matrix(self, obj_2):
        if len(self.matrix[0]) != len(obj_2.matrix):
            print("Imposible to multiply these matrixes!")
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for i_2 in range(len(obj_2.matrix[0])):
                sum = 0
                for j in range(len(self.matrix[i])):
                    sum += self.matrix[i][j] * obj_2.matrix[j][i_2]
                result[i].append(sum)
        self.matrix = result



    def operations(self, obj_2, oper):
        if type(obj_2) == MatrixClass:
            if oper == "+":
                self.__add_matrix(obj_2)
            elif oper == "-":
                self.__sub_matrix(obj_2)
            elif oper == "*":
                self.__mul_matrix(obj_2)
            else:
                print("unknown operation")
                return None
        elif type(obj_2) == int or type(obj_2) == float:
            if oper == "+":
                self.__add_digit(obj_2)
            elif oper == "-":
                self.__sub_digit(obj_2)
            elif oper == "*":
                self.__mul_digit(obj_2)
            else:
                print("unknown operation")
                return None
        else:
            print("object from operation with matrix must be digit or matrix")
            return None


    def tranponation(self):
        columns = 0
        lines = 0
        if len(self.matrix) > len(self.matrix[0]):
            columns = len(self.matrix) - len(self.matrix[0])
            for i in range(len(self.matrix)):
                for j in range(columns):
                    self.matrix[i].append(0)
        elif  len(self.matrix) < len(self.matrix[0]):
            lines = len(self.matrix[0]) - len(self.matrix)
            for i in range(lines):
                self.matrix.append([0 for j in range(len(self.matrix[0]))])

        count = 0
        for i in range(len(self.matrix)):
            for j in range(count, len(self.matrix[i])):
                if i != j:

                        self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
            count += 1
        if columns > 0:
            for i in range(columns):
                self.matrix.pop()
        elif lines > 0:
            for i in range(len(self.matrix)):
                for j in range(lines):
                    self.matrix[i].pop()


try:
    list_1 = [[1, 2, 3, 11, 12, 13], [4, 5, 6, 14, 15, 16]]
    list_2 = [[1, 2], [4, 5], [7, 8]]
    matrix_ = MatrixClass(list_1)
    matrix_2 = MatrixClass(list_2)
    print(matrix_.__str__())
    print(matrix_2.__str__())
    # matrix_.operations(matrix_2, "*")
    #
    # print(f"\n"*2)

    matrix_2.tranponation()
    print(matrix_2.__str__())

except AttributeError:
    None