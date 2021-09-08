"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not
share common letters. If no such two words exist, return 0.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        prod = 0
        length = len(words)
        for i in range(length):
            for j in range(i+1, length):
                if not self.shareLetter(words[i], words[j]):
                    tmp = len(words[i]) * len(words[j])
                    if tmp > prod:
                        prod = tmp
        return prod

    def shareLetter(self, str1, str2):
        for ch in str1:
            if ch in str2: return True
        else: return False



if __name__ == "__main__":
    words = ["a","aa","aaa","aaaa"]
    s = Solution()
    r = s.maxProduct(words)
    print(r)