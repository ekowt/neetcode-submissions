class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word2 = ''
        for s in word:
            if s.isalpha() or s.isdigit():
                word2+=s
        
        print(word2)
        a=0
        b=len(word2)-1

        while a <=  b:
            if(word2[a] != word2[b]):
                return False
            a+=1
            b-=1
        
        return True

