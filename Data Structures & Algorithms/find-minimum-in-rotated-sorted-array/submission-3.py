class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        nums.sort()
        r= len(nums)-1
        while l<=r:
            mid = (l+r//2)
            if nums[mid] < nums[l]:
                l+=1
            elif nums[mid] > nums[r]:
                r-=1
            else:
                return nums[l]