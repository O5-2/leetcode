class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        increase = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                a = [grid[i][(j+x)%len(grid)] for x in range(1, len(grid))]
                b = [grid[(i+x)%len(grid)][j] for x in range(1, len(grid))]
                increase += max(grid[i][j], min(max(a), max(b)))-grid[i][j]
        return increase
