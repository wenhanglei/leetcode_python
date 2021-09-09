"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round,
you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.
"""


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        bulbs = [True] * n
        for i in range(2, n+1):
            for j in range(i, n+1, i):
                bulbs[j-1] = not bulbs[j-1]
        r = 0
        for i in range(n):
            if bulbs[i]: r +=1
        return r




if __name__ == "__main__":
    sol = Solution()
    r = sol.bulbSwitch(4)
    print(r)