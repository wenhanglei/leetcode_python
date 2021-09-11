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
        self.hight = 0
        if self.traverse(coins, amount, 0):
            return self.hight
        return -1


    def traverse(self, coins, amount, depth):
        if amount == 0:
            if self.hight == 0:
                self.hight = depth
            elif depth < self.hight:
                self.hight = depth
            return True
        elif amount < 0:
            return False
        else:
            isValid = False
            for coin in coins:
                if amount >= coin and self.traverse(coins, amount - coin, depth+1):
                    isValid = True
            return isValid



if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 100
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(r)