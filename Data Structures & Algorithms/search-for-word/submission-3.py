class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visit = set()

        def dfs(i,r,c):
            if  i == len(word):
                return True
            if(r < 0 or c< 0 or r>=rows or c>=cols or word[i]!= board[r][c] or (r,c) in visit):
                return False
            
            visit.add((r,c))
            res = (dfs(i+1,r+1,c)or
                  dfs(i+1,r-1,c)or
                  dfs(i+1,r,c+1)or
                  dfs(i+1,r,c-1))
            visit.remove((r,c))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(0,i,j):
                    return True
        return False
                    