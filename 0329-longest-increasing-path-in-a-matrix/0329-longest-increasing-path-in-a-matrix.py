class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp=[]
        dp = [[-1 for _ in range(m)]  for _ in range(n)]
        return self.solve(matrix, n, m,dp)

    def solve(self, l: list[list[int]], n: int, m: int,dp:list[list[int]]):
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, self.helper(l, i, j, n, m,dp))
        return 1 + ans

    def helper(self, l, i, j, n, m,dp):
        if i >= n or j >= m or i < 0 or j < 0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j] 
        a = 0
        if i + 1 < n and l[i][j] < l[i + 1][j]:
            a = 1 + self.helper(l, i + 1, j, n, m,dp)
        b = 0
        if i - 1 >= 0 and l[i][j] < l[i - 1][j]:
            b = 1 + self.helper(l, i - 1, j, n, m,dp)
        c = 0
        if j + 1 < m and l[i][j] < l[i][j + 1]:
            c = 1 + self.helper(l, i, j + 1, n, m,dp)
        d = 0
        if j - 1 >= 0 and l[i][j] < l[i][j - 1]:
            d = 1 + self.helper(l, i, j - 1, n, m,dp)
        dp[i][j]= max(a, b, c, d)
        return dp[i][j]