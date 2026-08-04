class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = []
        
        for i in range(len(temp)):
            count =1
            j = i+1
            while j<len(temp):
                if temp[j] > temp[i]:
                    break
                j+=1
                count+=1
            count = 0 if j == len(temp) else count
            res.append(count)
                
        return(res)
                