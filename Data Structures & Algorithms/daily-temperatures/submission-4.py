class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temps)

        l = 0
        for r in range(len(temps)):
            while stack and temps[r] > stack[-1][1] :
                    l,temp = stack.pop()
                    res[l] = r-l
                
            stack.append((r,temps[r]))

        return(res)
    