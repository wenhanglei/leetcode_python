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

    def dfs(self, s, i, graph, scanned, depth, depths):
        if scanned[i]:
            if depth >= depths[s]:
                depths[s] = depth
            return
        scanned[i] = True
        for j in graph[i]:
            self.dfs(s, j, graph, scanned, depth + 1, depths)

def test_graph():
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    s = Solution()
    r = s.graph(n, edges)
    for idx, i in enumerate(r):
        print("%s => %s" % (idx, i))

def test_dfs():
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    s = Solution()
    r = s.graph(n, edges)
    depths = [0] * n
    s.dfs(1, 1, r, [False]*n, 0, depths)
    print(depths[0])


if __name__ == "__main__":
    test_graph()
    print("="*20)
    test_dfs()
