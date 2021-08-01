"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 1
        lo = 0
        for i in range(len(nums)):
            if nums[i+1] > nums[i]:
                ret += 1

cases = [
    {
        "arg": [10, 9, 2, 5, 3, 7, 101, 18],
        "expect": 4
    },
    {
        "arg": [7, 7, 7, 7, 7, 7, 7],
        "expect": 1
    },
    {
        "arg": [4, 10, 4, 3, 8, 9],
        "expect": 3
    },
]

if __name__ == "__main__":
    checkRet = True
    s = Solution()
    for case in cases:
        r = s.lengthOfLIS(case['arg'])
        print("Input: nums = %s" % case['arg'])
        print("Output: %s" % r)
        if checkRet:
            assert r == case['expect']
