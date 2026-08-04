class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        visit = set(nums)
        total = 0
        for i in nums:
            if i-1 not in visit:
                n = 1
                while i+n in visit:
                    n+=1
                total = max(total,n)
                
        return(total)
                