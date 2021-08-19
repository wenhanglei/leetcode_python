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
        v = [[]] * n
        for i, j in edges:
            v[i].append(j)
        depths = [0] * n
        for i in range(n):
            self.dfs(i, v, [False] * n, 1, depths)
        m = min(*depths)
        return [idx for idx, i in enumerate(depths) if i == m]

    def dfs(self, i, graph, scaned, depth, depths):
        if scaned[i]:
            if depth >= depths[i]:
                depths[i] = depth
            return
        scaned[i] = True
        for j in graph[i]:
            self.dfs(j, graph, scaned, depth+1, depths)
        if depth >= depths[i]:
            depths[i] = depth



if __name__ == "__main__":
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    s = Solution()
    s.findMinHeightTrees(n, edges)
