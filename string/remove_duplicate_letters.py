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
        ret = []
        last_index = {}
        for idx, i in enumerate(s):
            last_index[i] = idx
        for idx, i in enumerate(s):
            self.handle(ret, i, idx, last_index)
            if i not in ret:
                ret.append(i)
        return ''.join(ret)

    def handle(self, ret, key, curIndex, lastIndex):
        if ret and key not in ret and key < ret[-1] and lastIndex[ret[-1]] > curIndex:
            del ret[-1]
            self.handle(ret, key, curIndex, lastIndex)






if __name__ == "__main__":
    s = "abacb"
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(r)

