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
        keys = [i for i in m]
        self.text = None
        self.traverse(keys, 0, m, [], list(s))
        return self.text

    def traverse(self, keys, next, m, r, l):
        if next >= len(keys):
            t = self.merge(r[:], l)
            if self.text is None:
                self.text = t
            else:
                self.text = min(self.text, t)
            return
        for i in m[keys[next]]:
            r.append(i)
            self.traverse(keys, next+1, m, r, l)
            del r[-1]

    def merge(self, l, o):
        l.sort()
        return ''.join([o[i] for i in l])


if __name__ == "__main__":
    s = "cbacdcbc"
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(r)

