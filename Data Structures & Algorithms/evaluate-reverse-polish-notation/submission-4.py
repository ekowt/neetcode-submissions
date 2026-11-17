class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return
        if len(tokens) == 1 and tokens[0].isdigit():
            return int(tokens[0])
        x,y =0,0
        res = 0
        stack = []
        mapper = {'+','-','*','/'}
        
        for i in tokens:
            if i not in mapper:
                stack.append(int(i))
            
            if i == '+':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x+y)
            elif i == '-':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y-x)
            elif i == '*':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x*y)
            elif i == '/':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(int(y/x))
        
        return(stack[0])