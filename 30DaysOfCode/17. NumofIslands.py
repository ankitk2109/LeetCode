class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def markIsland(i,j):
            
            if( i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='2' or grid[i][j]=='0'):
                return
            
            grid[i][j] = '2'
            markIsland(i + 1, j)
            markIsland(i - 1, j)
            markIsland(i, j + 1)
            markIsland(i, j - 1)
        
        
        if not grid:
            return 0 
        
        no_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    no_of_islands += 1
                    markIsland(i,j)
        return no_of_islands