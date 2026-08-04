class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        word1  = sorted(s)
        word2 = sorted(t)
        return(word1 == word2)