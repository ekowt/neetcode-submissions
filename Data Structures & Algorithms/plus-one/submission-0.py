class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits
        for i in range(len(res)-1,-1,-1):
            if res[i] < 9:
                res[i]+=1
                return res
            else:
                res[i]= 0
        
        res.insert(0,1)
        return(res)
    
