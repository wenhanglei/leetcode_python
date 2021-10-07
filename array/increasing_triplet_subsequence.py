"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i]
< nums[j] < nums[k]. If no such indices exists, return false.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #尝试使用贪心算法求解

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    ret = sol.increasingTriplet(nums)
    print(ret)