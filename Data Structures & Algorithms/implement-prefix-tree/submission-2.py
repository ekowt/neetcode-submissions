class Node():
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
       self.root = Node()

    def insert(self, word: str) -> None:
        cur  = self.root
        for n in word:
            if n not in cur.children:
                cur.children[n] = Node()
            cur = cur.children[n]
        cur.word = True
            


    def search(self, word: str) -> bool:
        cur  = self.root
        for n in word:
            if n not in cur.children:
                return False
            cur = cur.children[n]
        return cur.word
        
    
    def startsWith(self, prefix: str) -> bool:
        
        cur  = self.root
        for n in prefix:
            if n not in cur.children:
                return False
            cur = cur.children[n]
        return True
       
    
        