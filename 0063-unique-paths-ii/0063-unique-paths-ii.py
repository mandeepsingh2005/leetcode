class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp=[]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp =[[0]*n for _ in range(m)]
        if obstacleGrid[m-1][n-1]==1:
            return 0
        for i in range(m-1,-1,-1):
            if obstacleGrid[i][n-1]==1:
                break
            dp[i][n-1]=1
        for j in range(n-2,-1,-1):
            if obstacleGrid[m-1][j]==1:
                break
            dp[m-1][j]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]==1:
                    dp[i][j]==0
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]