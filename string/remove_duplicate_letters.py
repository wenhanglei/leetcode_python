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
        m = {}
        for idx, i in enumerate(s):
            if i not in m:
                m[i] = []
            m[i].append(idx)
        li = list(s)
        for i in m:
            if len(m[i]) > 1:
                temp = li[:]



if __name__ == "__main__":
    s = "cbacdcbc"
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(r)

