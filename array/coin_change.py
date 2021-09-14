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
        nums = {}
        self.traverse(coins, amount, nums)
        return nums[amount]

    def traverse(self, coins, amount, nums):
        if amount in nums:
            return nums[amount]
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        r = -1
        for coin in coins:
            tmp = self.traverse(coins, amount-coin, nums)
            if tmp != -1:
                if r == -1 or tmp < r:
                    r = tmp
        if r == -1:
            return -1
        nums[amount] = r+1
        return r+1





if __name__ == "__main__":
    coins = [186,419,83,408]
    amount = 6249
    sol = Solution()
    r = sol.coinChange(coins, amount)
    print(r)