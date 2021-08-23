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
            return []
        g = self.graph(n, edges)
        depths = [0] * n
        for i in range(n):
            self.dfs(i, i, g, [False]*n, 1, depths)
        mi = min(*depths)
        return [idx for idx, i in enumerate(depths) if i == mi]

    def graph(self, n, edges):
        g = [None] * n
        for i, j in edges:
            if g[i] is None:
                g[i] = []
            if g[j] is None:
                g[j] = []
            g[i].append(j)
            g[j].append(i)
        return g

    def dfs(self, o, n, g, flags, depth, depths):
        flags[n] = True
        for v in g[n]:
            if not flags[v]:
                self.dfs(o, v, g, flags, depth+1, depths)
        if depth > depths[o]:
            depths[o] = depth


