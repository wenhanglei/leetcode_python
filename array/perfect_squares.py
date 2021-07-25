"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        pass


    def isSquare(self, n):
        for i in range(n):
            if i * i == n:
                return True
            elif i * i < n:
                continue
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append(12)
    cases.append(13)
    for case in cases:
        ret = s.numSquares(case)
        print("Input: n = %s" % case)
        print("Output: %s" % ret)
