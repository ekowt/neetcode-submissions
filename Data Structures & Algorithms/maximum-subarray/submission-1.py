class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total,cur = nums[0],0

        for num in nums:
            if cur < 0:
                cur = 0
            cur+=num
            total = max(cur,total)
        return(total)
        
