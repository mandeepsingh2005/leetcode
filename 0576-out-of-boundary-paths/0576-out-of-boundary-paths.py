class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        dp = {}
        def solve(row, col, moves):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if moves == 0:
                return 0
            if (row, col, moves) in dp:
                return dp[(row, col, moves)]
            ans = (
                solve(row - 1, col, moves - 1) +
                solve(row + 1, col, moves - 1) +
                solve(row, col - 1, moves - 1) +
                solve(row, col + 1, moves - 1)
            )
            dp[(row, col, moves)] = ans % MOD
            return dp[(row, col, moves)]
        return solve(startRow, startColumn, maxMove)