"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
result is the smallest in lexicographical order among all possible results.
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = set(s)
        l = list(r)
        return ''.join(l)


if __name__ == "__main__":
    s = "bcabc"
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(r)