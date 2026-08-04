class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for c in s:
            if res and  c == ')' and res[-1] == '(':
                res.pop()
            elif res and  c == '}' and res[-1] == '{':
                res.pop()
            elif res and  c == ']' and res[-1] == '[':
                res.pop()
            else:
                res.append(c)
        
        return(len(res) == 0)