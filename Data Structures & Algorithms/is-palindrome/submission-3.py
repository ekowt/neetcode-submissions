class Solution:
    def isPalindrome(self, s: str) -> bool:
        word =""
        for c in s:
            if c.isalpha() or c.isdigit():
                word+=c
        word = word.lower()
        print(word)
        a =0
        b = len(word)-1
        while a<=b:
            if word[a]!=word[b]:
                return False
            a+=1
            b-=1
        return True