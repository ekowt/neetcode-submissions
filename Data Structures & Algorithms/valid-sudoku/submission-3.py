class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        ## for rows
        for i in range(rows):
            visit = set()
            for j in range(cols):
                if board[i][j] in visit:
                    return False
                if board[i][j] != '.':
                    visit.add(board[i][j])
    
        ## for col
        for j in range(cols):
            visit = set()
            for i in range(rows):
                if board[i][j] in visit:
                    return False
                if board[i][j] != '.':
                    visit.add(board[i][j])

        ## for each 3x3
        for i in range(0,9,3):
            for j in range(0,9,3):
                visit = set()
                for row in range(3):
                    for col in range(3):
                        if board[i+row][j+col] in visit:
                            return False
                        if board[i+row][j+col] != '.':
                            visit.add(board[i+row][j+col])

        return True