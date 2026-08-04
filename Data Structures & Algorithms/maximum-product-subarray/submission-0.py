class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        total = nums[0]
        
        for i in range(len(nums)):
            cur = nums[i]
            total = max(cur,total)
            for j in range(i+1,len(nums)):
                cur *= nums[j]
                total = max(cur,total)
        return total
        

