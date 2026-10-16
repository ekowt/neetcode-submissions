class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapper = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapper:
                return [mapper[comp]+1,i+1]
            else:
                mapper[nums[i]] = i
      
        