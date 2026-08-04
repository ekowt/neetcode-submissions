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
        cur.word =True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        node = Node()

        for word in words:
            node.add(word)

        visit = set()
        res = set()
        row = len(board)
        col = len(board[0])
        def dfs(r,c,node,word):

            if r<0 or c<0 or r>=row or c>=col or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.word:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
            

     
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,node,"")
        
        return list(res)

        