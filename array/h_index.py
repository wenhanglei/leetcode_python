"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h
citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations.reverse()
        for i in range(len(citations)):
            if i + 1 >= citations[i]:
                return max(citations[i], i)
        return len(citations)


if __name__ == "__main__":
    s = Solution()
    cases = []
    cases.append([0, 0, 0, 0])
    cases.append([100, 50])
    cases.append([100])
    cases.append([4, 4, 0, 0])
    for case in cases:
        ret = s.hIndex(case)
        print("Input: citations = %s" % case)
        print("Output: %s" % ret)
