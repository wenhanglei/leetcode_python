"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""


class Solution(object):

    def __init__(self):
        self.max = 1

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.max = 1
        m = len(nums)
        for i in range(m):
            self.traverse(nums, i, m, 1)
        return self.max

    def traverse(self, nums, i, m, depth):
        curr = nums[i]
        for j in range(i+1, m):
            if nums[j] > curr:
                self.traverse(nums, j, m, depth+1)
        if depth > self.max:
            self.max = depth



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
    {
        "arg": [0, 1, 0, 3, 2, 3],
        "expect": 4
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
