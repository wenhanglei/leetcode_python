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
        l = {i ** 2: 1 for i in range(1, n+1) if i ** 2 <= n}
        m = [i ** 2 for i in range(1, n+1) if i ** 2 <= n]
        if m[-1] == n:
            return 1
        for i in range(2, n+1):
            self.search(l, m, i, i, 0, n)
            if n in l:
                return l[n]

    def search(self, l, m, num, count, ret, limit):
        if ret > limit:
            return
        elif count == 0:
            if ret not in l:
                l[ret] = num
            return
        else:
            for i in m:
                self.search(l, m, num, count - 1, i + ret, limit)


if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append(7168)
    for case in cases:
        ret = s.numSquares(case)
        print("Input: n = %s" % case)
        print("Output: %s" % ret)
