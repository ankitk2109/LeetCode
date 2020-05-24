class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[float('inf')] * (cols + 1) for i in range(rows + 1)] #creating a grid with extra row and col for ease of calculation.
        dp[0][1], dp[1][0] = 0,0
        
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1]) #We can only me to right or in downward direction

        return(dp[rows][cols])
        
        