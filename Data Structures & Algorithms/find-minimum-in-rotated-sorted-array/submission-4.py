class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        nums.sort()
        
        return nums[l]