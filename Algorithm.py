import copy
import numpy as np

class BasicMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
    
    def determinant(self):
        if self.row == 1:
            return self.matrix[0][0]
        if self.row == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            det = 0
            positive = True
            for i in range(self.col):
                new_matrix = copy.deepcopy(self.matrix)
                new_matrix.pop(0)
                for j in range(len(new_matrix)):
                    new_matrix[j].pop(i)
                tmp = BasicMatrix(new_matrix)
                if positive:
                    det += self.matrix[0][i] * tmp.determinant()
                    positive = False
                else:
                    det -= self.matrix[0][i] * tmp.determinant()
                    positive = True
            return det

class GaussJordan(BasicMatrix):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.l = [[0 for _ in range(self.col)] for _ in range(self.row)]
        if (self.row != self.col):
            raise Exception("A mátrix nem n x n")
    def can_be_solved(self):
        return self.determinant() != 0


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    gj = GaussJordan(matrix)
    print(gj.determinant())
    print(gj.can_be_solved())
    matrix = [[3,8], [3,6]]
    gj = GaussJordan(matrix)
    print(gj.determinant())
    print(gj.can_be_solved())

if __name__ == '__main__':
    main()