class Node:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def add(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True
    
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        tree = Node()
        res = set()

        for word in words:
            tree.add(word)
      
        def dfs(r,c,tree,word):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c] not in tree.children:
                return
            
            visit.add((r,c))
            tree = tree.children[board[r][c]]
            word+=board[r][c]
            if tree.word:
                res.add(word)
            dfs(r+1,c,tree,word)
            dfs(r-1,c,tree,word)
            dfs(r,c+1,tree,word)
            dfs(r,c-1,tree,word)
            visit.remove((r,c))
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,tree,"")
        
        return(list(res))

        