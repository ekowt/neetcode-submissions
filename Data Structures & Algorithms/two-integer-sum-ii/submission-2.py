class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        a=0
        b=len(nums)-1

        while a<b:
            sum = nums[a]+nums[b]
            if sum < target:
                a+=1
            elif sum > target:
                b-=1
            else:
                return [a+1,b+1]
        return []