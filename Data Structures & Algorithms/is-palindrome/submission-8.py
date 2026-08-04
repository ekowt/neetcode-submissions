class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ''
        s = s.lower()
        for  i  in s:
            if i.isalpha() or i.isdigit():
                word+=i
        

        a = 0
        b = len(word)-1
        while a < b :
            if word[a] != word[b]:
                return False
            a+=1
            b-=1
        return True