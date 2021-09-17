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
        for i in range(len(nums)-1):
            if i%2 == 0:
                if nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i+1] > nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]


if __name__ == "__main__":
    nums = [5,5,5,4,4,4,4]
    s = Solution()
    s.wiggleSort(nums)
    print(nums)

