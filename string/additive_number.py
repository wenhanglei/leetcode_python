"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent
number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
"""


class Solution(object):

    def __init__(self):
        self.r = False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)):
            prepre = int(num[0:i])
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, len(num)):
                if num[i] == '0' and j - i > 1:
                    break
                pre = int(num[i:j])
                if self.fun(num[j:], prepre, pre):
                    return True
        return False

    def fun(self, num, prepre, pre):
        if not num:
            return True
        sum = prepre + pre
        if num.startswith(str(sum)):
            return self.fun(num[len(str(sum)):], pre, sum)
        else:
            return False






if __name__ == "__main__":
    num = "0235813"
    s = Solution()
    r = s.isAdditiveNumber(num)
    print("Input: %s" % num)
    print("Output: %s" % r)
