class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None] * n for _ in range(m)]
        ans = float('inf')
        for j in range(n):
            ans = min(ans, self.solve(matrix, 0, j, m, n, dp))
        return ans
    def solve(self, l, i, j, m, n, dp):
        if i < 0 or j < 0 or i >= m or j >= n:
            return float('inf')
        if i == m - 1:
            return l[i][j]
        if dp[i][j] is not None:
            return dp[i][j]
        a = self.solve(l, i + 1, j - 1, m, n, dp)
        b = self.solve(l, i + 1, j + 1, m, n, dp)
        c = self.solve(l, i + 1, j, m, n, dp)
        dp[i][j] = l[i][j] + min(a, b, c)
        return dp[i][j]