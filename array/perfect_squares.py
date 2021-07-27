"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""
n = 10 ** 4
l = {i ** 2: 1 for i in range(1, n + 1) if i ** 2 <= n}
m = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]

for p in range(5):
    for i in list(l.keys())[:]:
        for k in m:
            if i+k not in l:
                l[i+k] = l[i]+1



class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return l[n]


if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append(12)
    cases.append(13)
    cases.append(7168)
    for case in cases:
        ret = s.numSquares(case)
        print("Input: n = %s" % case)
        print("Output: %s" % ret)
