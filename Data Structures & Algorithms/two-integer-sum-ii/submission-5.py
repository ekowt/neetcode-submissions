class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = 0
        b = len(nums)-1

        while a < b:
            total = nums[a] + nums[b]
            if total > target :
                b-=1
            elif total < target :
                a+=1
            else:
                return [a+1,b+1]

        return 0
