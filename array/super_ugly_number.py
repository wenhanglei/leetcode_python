"""
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        l = [1]
        for k in range(n - 1):
            current = l[-1]
            idx = len(l)-1
            m = current
            for j in primes:
                while idx >= 0:
                    if j * l[idx] <= current:
                        break
                    idx -= 1
                if m == current:
                    m = j * l[idx+1]
                elif j * l[idx+1] < m:
                    m = j * l[idx+1]
            l.append(m)
        return l[-1]


if __name__ == "__main__":
    n = 12
    primes = [2, 7, 13, 19]
    s = Solution()
    r = s.nthSuperUglyNumber(n, primes)
    print(r)
