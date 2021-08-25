"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected
graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that
there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the
root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with
minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        if len(edges) == 1:
            return edges[0]
        degree = [0] * n
        for i, j in edges:
            degree[i] += 1
            degree[j] += 1
        leaves = [idx for idx, i in enumerate(degree) if i == 1]
        nonleaves = [idx for idx, i in enumerate(degree) if i > 1]
        if len(nonleaves) <= 2:
            return nonleaves
        else:
            left = []
            for edge in edges:
                for i in leaves:
                    if i in edge:
                        break
                else:
                    left.append(edge)
            return self.findMinHeightTrees(n, left)






