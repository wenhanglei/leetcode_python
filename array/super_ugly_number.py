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
        if len(primes) == 1:
            return primes[0] ** (n-1)
        l = primes[:]
        for i in range(n-2):
            (idx, j) = self.minimal(l)
            print(j)
            l[idx] = j * primes[0]
        return min(*l)

    def minimal(self, n):
        mi = min(*n)
        for idx, i in enumerate(n):
            if i == mi:
                return idx, i


if __name__ == "__main__":
    n = 15
    primes = [3,5,7,11,19,23,29,41,43,47]
    s = Solution()
    r = s.nthSuperUglyNumber(n, primes)
    print(r)
