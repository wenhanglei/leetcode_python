"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set()
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                return num



if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append([1, 3, 4, 2, 2])
    cases.append([3, 1, 3, 4, 2])
    cases.append([1, 1, 2])
    cases.append([1, 1])
    for case in cases:
        ret = s.findDuplicate(case)
        print("Input: nums = %s" % case)
        print("Output: %s" % ret)
