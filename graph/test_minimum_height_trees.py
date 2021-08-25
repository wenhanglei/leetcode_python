from minimum_height_trees import Solution

s = Solution()
# n = 6
# edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]


if __name__ == "__main__":
    r = s.findMinHeightTrees(n, edges)
    print(r)

