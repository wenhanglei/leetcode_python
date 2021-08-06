"""
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        self.sum = 0
        for i in nums:
            self.sum += i

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.sum -= (self.nums[index] -val)
        self.nums[index] = val



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if(right -left) > self.size // 2:
            sub1 = 0
            for i in range(left):
                sub1 += self.nums[i]
            sub2 = 0
            for i in range(right+1, self.size):
                sub2 += self.nums[i]
            return self.sum-sub1-sub2
        else:
            sum = 0
            for i in range(left, right+1):
                sum += nums[i]
            return sum

if __name__ == "__main__":
    nums = [1, 3, 5]
    s = NumArray(nums)
    r = s.sumRange(0, 2)
    s.update(1, 2)
    r = s.sumRange(0, 2)
    print(r)
