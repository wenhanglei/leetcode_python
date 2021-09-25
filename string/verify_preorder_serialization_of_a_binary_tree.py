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
        nodes = preorder.split(',')
        st = []
        for i in nodes:
            st.append(i)
            while i == '#' and len(st) >= 3 and st[-1] == '#' and st[-2] == '#' and st[-3] != '#':
                st.pop()
                st.pop()
                st.pop()
                st.append('#')
        return len(st) == 1 and st[-1] == '#'




if __name__ == "__main__":
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    sol = Solution()
    r = sol.isValidSerialization(preorder)
    print(r)