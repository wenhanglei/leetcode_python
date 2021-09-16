"""
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == "__main__":
    nums = [1,5,1,1,6,4]
    s = Solution()
    s.wiggleSort(nums)
    print(nums)

