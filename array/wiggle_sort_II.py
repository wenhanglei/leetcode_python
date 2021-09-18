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
        nums.sort(reverse=True)
        size = len(nums)
        limit = size // 2
        itl = iter(nums[:limit])
        itr = iter(nums[limit:])
        for i in range(size):
            nums[i] = next(itr) if i % 2 == 0 else next(itl)



if __name__ == "__main__":
    nums = [4,5,5,6]
    s = Solution()
    s.wiggleSort(nums)
    print(nums)

