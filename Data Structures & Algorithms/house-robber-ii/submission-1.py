class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
       
        

        def dfs(nums):
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
        
            
            dp1= [0]*n
            dp1[0] = nums[0]
            dp1[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp1[i] = max(dp1[i-1],nums[i]+dp1[i-2])
            return(dp1[-1])

        return(max(dfs(nums[1:]), dfs(nums[:-1])))

        
        
        