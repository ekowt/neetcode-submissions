class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack= []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        """ 
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.minstack[-1]
