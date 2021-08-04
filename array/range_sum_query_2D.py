"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower
 right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
 defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        self.m = []
        for i in range(rows):
            self.m.append([])
            pre = 0
            for j in range(cols):
                self.m[i].append(matrix[i][j] + (self.m[i-1][j] if i >= 1 else 0) + pre)
                pre += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 >= 1 and col1 >= 1:
            return self.m[row2][col2] - self.m[row1-1][col2] - self.m[row2][col1-1] + self.m[row1-1][col1-1]
        elif row1 >=1:
            return self.m[row2][col2] - self.m[row1-1][col2]
        elif col1 >=1:
            return self.m[row2][col2] - self.m[row2][col1-1]
        else:
            return self.m[row2][col2]


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    s = NumMatrix(matrix)
    r = s.sumRegion(2, 1, 4, 3)
    r1 = s.sumRegion(1, 1, 2, 2)
    print(r)
    print(r1)
