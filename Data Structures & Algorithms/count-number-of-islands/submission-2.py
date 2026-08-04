class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(grid,r,c):
            if r<0 or c<0 or r>= rows or c>= cols or grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            dfs(grid,r+1,c)
            dfs(grid,r-1,c)
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    count+=1
        return count
                