class Node:
    def __init__(self):
        self.children= {}
        self.word =False
class WordDictionary:

    def __init__(self):
        self.node = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(index,node):

            if index == len(word):
                return node.word
            
            c = word[index]
            if c == '.':
                for child in node.children.values():
                    if dfs(index+1,child):
                        return True
                    return False
            else:
                if c not in node.children:
                    return False
                return dfs(index+1,node.children[c])
        return dfs(0,self.node)
            
        

        
