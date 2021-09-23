"""
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the
node's value. If it is a null node, we record using a sentinel value such as '#'.
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        li = preorder.split(',')
        if len(li) % 2 == 0:
            return False
        num = 0
        for ch in li:
            if ch == '#':
                num += 1
        if num != (len(li) + 1) // 2:
            return False
        return True




if __name__ == "__main__":
    preorder = "9,#,#,1"
    sol = Solution()
    r = sol.isValidSerialization(preorder)
    print(r)