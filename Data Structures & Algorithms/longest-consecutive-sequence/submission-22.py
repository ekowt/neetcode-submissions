class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 0
        visit = set(nums)
        res = 0

        for num in nums:
            if num -1 not in visit:
                length = 1
                while num+length in visit:
                    length+=1
                res = max(res,length)
        return(res)