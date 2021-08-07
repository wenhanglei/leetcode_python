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
        for i in range(len(prices)):
            pass

    def buy(self, prices, i, p):
        pass

    def sell(self, prices, i):
        pass


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    s = Solution()
    r = s.maxProfit(prices)
    print(r)