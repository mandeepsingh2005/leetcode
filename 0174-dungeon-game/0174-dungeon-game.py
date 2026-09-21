class Solution:
    def calculateMinimumHP(self, dungeon):
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[-1] * cols for _ in range(rows)]
        def find(i, j):
            if i == rows - 1 and j == cols - 1:
                return max(1, 1 - dungeon[i][j])
            if dp[i][j] != -1:
                return dp[i][j]
            down = float('inf')
            if i + 1 < rows:
                down = find(i + 1, j)
            right = float('inf')
            if j + 1 < cols:
                right = find(i, j + 1)
            need = min(down, right) - dungeon[i][j]
            dp[i][j] = max(1, need)
            return dp[i][j]
        return find(0, 0)