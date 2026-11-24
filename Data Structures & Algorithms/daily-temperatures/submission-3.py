class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [(0,temps[0])]
        res = [0]*len(temps)

        l = 0
        for r in range(1,len(temps)):
            while stack and temps[r] > stack[-1][1] :
                    l,temp = stack.pop()
                    res[l] = r-l
                
            stack.append((r,temps[r]))

        return(res)
    