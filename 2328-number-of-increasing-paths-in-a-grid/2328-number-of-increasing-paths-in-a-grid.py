class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 1000000007
        dp = [[-1] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += self.solve(grid, i, j, m, n, dp)
                ans %= mod
        return ans
    def solve(self, l, i, j, m, n, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 1  
        if i < m - 1 and l[i][j] < l[i + 1][j]:
            ans += self.solve(l, i + 1, j, m, n, dp)
        if i > 0 and l[i][j] < l[i - 1][j]:
            ans += self.solve(l, i - 1, j, m, n, dp)
        if j < n - 1 and l[i][j] < l[i][j + 1]:
            ans += self.solve(l, i, j + 1, m, n, dp)
        if j > 0 and l[i][j] < l[i][j - 1]:
            ans += self.solve(l, i, j - 1, m, n, dp)
        dp[i][j] = ans % 1000000007
        return dp[i][j]