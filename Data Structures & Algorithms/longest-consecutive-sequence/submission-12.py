class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        visit = set(nums)
        res = 0
        
        for num in visit:
            if num-1 not in visit:
                longest =1
                while (num+longest) in visit:
                    longest +=1
                res = max(longest,res)
        
        return(res)