"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead
(represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        w = len(board)
        h = len(board[0])
        r = []
        for i in range(w):
            r.append([])
            for j in range(h):
                temp = self.cul(i, j, w, h, board)
                if board[i][j] == 1 and temp < 2:
                    r[i].append(0)
                elif board[i][j] == 0 and temp == 3:
                    r[i].append(1)
                elif board[i][j] == 1 and temp > 3:
                    r[i].append(0)
                else:
                    r[i].append(board[i][j])
        for i in range(w):
            for j in range(h):
                board[i][j] = r[i][j]

    def cul(self, row, col, w, h, board):
        sum = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if (i == row and j == col) or i < 0 or j < 0 or i >= w or j >= h:
                    continue
                else:
                    sum += board[i][j]
        return sum


if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    cases.append([[1,1],[1,0]])
    for case in cases:
        ret = s.gameOfLife(case)
        print("Input: citations = %s" % case)
        print("Output: %s" % ret)