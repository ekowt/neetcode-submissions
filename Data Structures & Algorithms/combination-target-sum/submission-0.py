class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combs = []
        helper(0,[],combs,nums,target)
        return combs

def helper(i,curcombs,combs,nums,target):
    if sum(curcombs) == target:
        combs.append(curcombs.copy())
        return
    
    if sum(curcombs) > target or i >= len(nums):
        return
    
    curcombs.append(nums[i])
    helper(i,curcombs,combs,nums,target)
    curcombs.pop()

    helper(i+1,curcombs,combs,nums,target)


