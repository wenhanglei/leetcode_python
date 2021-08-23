from minimum_height_trees import Solution

s = Solution()
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

def test_graph():
    r = s.graph(n, edges)
    for idx, i in enumerate(r):
        print("%s => %s" % (idx, i))

def test_dfs():
    g = s.graph(n, edges)
    depths = [0] * n
    s.dfs(4, 4, g, [False] * n, 1, depths)
    print(depths[4])

def test_findMinHeightTrees():
    n = 1
    edges = []
    ret = s.findMinHeightTrees(n, edges)


if __name__ == "__main__":
    test_findMinHeightTrees()

