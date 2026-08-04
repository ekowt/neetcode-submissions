class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        glomin, glomax = nums[0] ,nums[0]
        curmin, curmax = 0,0
        total = 0

        for n in nums:
            curmax = max(curmax+n,n)
            curmin = min(curmin+n,n)
            total+=n
            glomax = max(curmax,glomax)
            glomin = min(curmin,glomin)
        
        return max(total-glomin, glomax) if glomax > 0 else glomax