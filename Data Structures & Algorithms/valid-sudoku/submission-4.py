class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        row = len(board)
        col = len(board[0])
        
        
        #1.Each Row without duplicates
        for i in range(row):
            visit = set()
            for j in range(col):
                if (board[i][j].isdigit() and board[i][j] in visit):
                    return False
                visit.add(board[i][j])
        
        #2.Each col without duplicates
        for i in range(row):
            visit = set()
            for j in range(col):
                if (board[j][i].isdigit() and board[j][i] in visit):
                    return False
                visit.add(board[j][i])
        
       
        
        
        #2.Each 3*3 without duplicates
        for i in range(0,9,3):
            for j in range(0,9,3):
               visit = set()
               for k in range(3):
                for l in range(3):
                    if (board[k+i][l+j].isdigit() and board[k+i][l+j] in visit):
                        return False
                    visit.add(board[k+i][l+j])
        
        return True
        

            