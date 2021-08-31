"""
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            nv = next(merged)
            if nv != uglies[-1]:
                uglies.append(nv)
        return uglies[-1]



if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    s = Solution()
    r = s.nthSuperUglyNumber(n, primes)
    print(r)
