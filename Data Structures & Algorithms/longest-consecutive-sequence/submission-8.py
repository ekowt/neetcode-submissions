class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit =set(nums)
        res = 0
    
    
        for num in visit:
            if num-1 not in visit:
                count =1
                while (num+1) in visit:
                    count+=1
                    num = num+1
                res=max(res,count)
        return(res)
          
                
        

        
