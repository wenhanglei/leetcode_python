"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        m = min(coins)
        size = amount // m
        checked = set()
        amts = list(coins)
        if amount in amts:
            return 1
        for i in range(2, size+1):
            tempAmts = []
            for amt in amts:
                for coin in coins:
                    val = amt+coin
                    if amount == val:
                        return i
                    if val not in checked:
                        checked.add(val)
                        tempAmts.append(val)
            amts = tempAmts
        return -1

if __name__ == "__main__":
    coins = [1]
    amount = 1
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(r)