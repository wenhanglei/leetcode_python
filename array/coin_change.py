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
        if amount == 0: return 0
        self.depth = 0
        coins.sort()
        return self.depth if self.traverse(coins[::-1], amount, 0) else -1

    def traverse(self, coins, amount, depth):
        if amount == 0:
            self.depth = depth
            return True
        elif amount < 0:
            return False
        else:
            for coin in coins:
                if amount >= coin:
                    if self.traverse(coins, amount-coin, depth+1):
                        return True
        return False




if __name__ == "__main__":
    coins = [186,419,83,408]
    amount = 6249
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(r)