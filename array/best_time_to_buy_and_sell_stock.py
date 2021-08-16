"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one
share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        s0, s1, s2 = [0] * size, [0] * size, [0] * size
        s0[0] = -prices[0]
        s1[0] = 0
        s2[0] = 0
        for i in range(1, size):
            s0[i] = max(s0[i - 1], s2[i - 1] - prices[i])
            s1[i] = s0[i - 1] + prices[i]
            s2[i] = max(s0[i - 1], s1[i - 1], s2[i - 1])
        return max(s1[-1], s2[-1])


if __name__ == "__main__":
    # prices = [1, 2, 3, 0, 2]
    prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72,
              15, 11, 94]
    # prices = [1]
    # prices = [2, 1]
    # prices = [1, 4, 2]
    # prices = [6, 1, 3, 2, 4, 7]
    s = Solution()
    r = s.maxProfit(prices)
    print(r)
