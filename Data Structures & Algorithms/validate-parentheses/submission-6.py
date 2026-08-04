class Solution:
    def isValid(self, s: str) -> bool:
        
        res = []
        for i in s:
            if res and i == ')' and res[-1] == '(':
                res.pop()
            elif res and i == '}' and res[-1] == '{':
                res.pop()
            elif res and i == ']' and res[-1] == '[':
                res.pop()
            else:
                res.append(i)
        
        return len(res) == 0
