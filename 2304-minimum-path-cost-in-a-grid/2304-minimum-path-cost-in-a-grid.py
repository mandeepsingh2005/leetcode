class Solution:
    def minPathCost(self, grid, moveCost):
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k]
                        + moveCost[grid[i - 1][k]][j]
                        + grid[i][j]
                    )
        return min(dp[m - 1])