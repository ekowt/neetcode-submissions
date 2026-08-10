class Solution:
    def isPalindrome(self, s: str) -> bool:

        word = ''
        for ch in s.lower():
            if ch.isalpha() or ch.isdigit():
                word+=ch
        
        a = 0
        b = len(word)-1

        while a<=b:
            if word[a] != word[b]:
                return False
            a+=1
            b-=1
        
        return True
        