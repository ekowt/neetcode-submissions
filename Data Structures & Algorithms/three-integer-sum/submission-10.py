class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
    
            a = i+1
            b = len(nums)-1
            
            while a < b:
                total = nums[i]+nums[a]+nums[b]
                if total > 0 :
                     b-=1
                elif total < 0:
                    a+=1
                else:
                    res.append([nums[i],nums[a],nums[b]])
                    a+=1
                    b-=1
                    while nums[a] == nums[a-1] and a<b:
                        a+=1
        return res