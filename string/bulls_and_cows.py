"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you
provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both
secret and guess may contain duplicate digits.
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = [True] * len(secret)
        b = [True] * len(guess)
        bulls = 0
        cows = 0
        for index, (i, j) in enumerate(zip(secret, guess)):
            if a[index] and i == j:
                bulls += 1
                a[index] = False
                b[index] = False
        for ix, i in enumerate(guess):
            if b[ix]:
                for idx, j in enumerate(secret):
                    if a[idx] and i == j:
                        cows += 1
                        a[idx] = False
                        b[ix] = False
                        break
        return "%sA%sB" % (bulls, cows)


cases = [
    {
        "origin": ("1123", "0111"),
        "expect": "1A1B"
    },
    {
        "origin": ("1807", "7810"),
        "expect": "1A3B"
    },
    {
        "origin": ("1", "0"),
        "expect": "0A0B"
    },
    {
        "origin": ("1", "1"),
        "expect": "1A0B"
    },
    {
        "origin": ("1", "1"),
        "expect": "1A0B"
    },
    {
        "origin": ("1122", "0001"),
        "expect": "0A1B"
    },
]

if __name__ == "__main__":
    checkResult = True
    s = Solution()
    for case in cases:
        a, b = case["origin"]
        ret = s.getHint(a, b)
        print("Input: secret \"%s\" , guess = \"%s\"" % (a, b))
        print("Output:\"%s\"" % ret)
        if checkResult:
            expect = case["expect"]
            if not ret == expect:
                raise Exception("Expected: %s Your result: %s" % (expect, ret))
