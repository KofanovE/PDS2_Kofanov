# Напишіть клас для роботи з матрицями. Клас повинен створювати об'єкт матриць з вкладених списків,
# виводити матриці на друк, виконувати операції додавання, віднімання, множення на число, множення на матрицю,
# транспонування. Передбачте можливість приведення матриці для операцій додавання і віднимання, та обробку виключних
# ситуацій для операції множення матриці на матрицю.

class MatrixClass:

    def __init__(self, obj):
        try:
            for i in range(len(obj)):
                if type(obj) == list and type(obj[i]) == list:
                    for j in obj[i]:
                        if not (type(j) == int or type(j) == float):
                            print("all elements of matrix must be digits")
                            self.matrix = [[]]
                            return None
                    self.matrix = obj
                else:
                    print("obj isn't list of lists")
                    self.matrix = [[]]
                    return None
        except TypeError:
            print("obj isn't list of lists")
            self.matrix = [[]]

    def __str__(self):
        return self.matrix




    def __add_digit(self, obj_2):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + obj_2)
        return MatrixClass(result)

    def __sub_digit(self, obj_2):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - obj_2)
        return MatrixClass(result)

    def __mul_digit(self, obj_2):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] * obj_2)
        return MatrixClass(result)

    def __del_digit(self, obj_2):
        try:
            result = []
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] + obj_2)
            return MatrixClass(result)
        except ZeroDivisionError:
            print("Error: divisor is zero!")
            return None


    def __add_matrix(self, obj_2):
        pass

    def __sub_matrix(self, obj_2):
        pass

    def __mul_matrix(self, obj_2):
        pass

    def __del_matrix(self, obj_2):
        pass

    def operations(self, obj_2, oper):
        if type(obj_2) == MatrixClass:
            if oper == "+":
                result = self.__add_matrix(obj_2)
            elif oper == "-":
                result = self.__sub_matrix(obj_2)
            elif oper == "*":
                result = self.__mul_matrix(obj_2)
            elif oper == "/":
                result = self.__del_matrix(obj_2)
            else:
                print("unknown operation")
                return None
        elif type(obj_2) == int or type(obj_2) == float:
            if oper == "+":
                result = self.__add_digit(obj_2)
            elif oper == "-":
                result = self.__sub_digit(obj_2)
            elif oper == "*":
                result = self.__mul_digit(obj_2)
            elif oper == "/":
                result = self.__del_digit(obj_2)
            else:
                print("unknown operation")
                return None
        else:
            print("object from operation with matrix must be digit or matrix")
            return None
        return result

    def tranponation(self):
        pass



list_ = [[1, 2, 3], [4, 5, 6]]
# list_ = ["a", 2, 3]
matrix_ = MatrixClass(list_)
matrix_2 = MatrixClass(list_)
print(matrix_.__str__())
print(type(matrix_.matrix))
# matrix_.operations(matrix_2, "+")
result = matrix_2.operations(2, '*')
print(result.matrix)



