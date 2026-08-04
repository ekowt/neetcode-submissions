class Solution {
    public int countPaths(int[][] grid) {
    
    int r = grid.length;
    int c = grid[0].length;
    int [][] visit = new int [r][c];
    return dfs(grid, 0,0,visit);

   
    }

    public int dfs(int[][]grid, int row, int col, int[][]visit)
    {
        if (row< 0 || col<0 || row == grid.length || col == grid[0].length ||
            visit[row][col] == 1 || grid[row][col] == 1 ) {
            return 0;
        }
        if(row == grid.length-1 && col == grid[0].length-1)
        {
            return 1;
        }

        visit[row][col] = 1;
        int count =0;
        count+= dfs(grid,row+1,col,visit);
        count+= dfs(grid,row-1,col,visit);
        count+= dfs(grid,row,col+1,visit);
        count+= dfs(grid,row,col-1,visit);

        visit[row][col]= 0;
        return count;
    }
}
