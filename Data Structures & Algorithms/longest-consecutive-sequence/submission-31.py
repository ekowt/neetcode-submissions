class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 0
        res = 0
        visit = set(nums)

        for i in nums:
            if i-1 not in visit:
                length =1
                while i+length in visit:
                    length+=1
            res = max(length, res)
        
        return(res)