class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapper= {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapper:
                print(mapper)
                return [mapper[comp],i]
            else:
                mapper[nums[i]] = i
        

            