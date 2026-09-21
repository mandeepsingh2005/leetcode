class Solution:
    def maxMoves(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1] * cols for _ in range(rows)]
        def find(i, j):
            if j == cols - 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = 0
            if i > 0 and grid[i - 1][j + 1] > grid[i][j]:
                ans = max(ans, 1 + find(i - 1, j + 1))
            if grid[i][j + 1] > grid[i][j]:
                ans = max(ans, 1 + find(i, j + 1))
            if i + 1 < rows and grid[i + 1][j + 1] > grid[i][j]:
                ans = max(ans, 1 + find(i + 1, j + 1))
            dp[i][j] = ans
            return ans
        answer = 0
        for i in range(rows):
            answer = max(answer, find(i, 0))
        return answer