class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visit = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in visit:
                return [visit[comp],i]
            visit[nums[i]] = i
        

        return []