class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        helper(comb, [], 0, nums,target)
        return comb
    
def helper(comb,curcomb,i,nums,target):
    if sum(curcomb) == target:
        comb.append(curcomb.copy())
        return
        
    if sum(curcomb) > target or i >= len(nums):
         return

    curcomb.append(nums[i])
    helper(comb,curcomb,i,nums,target)
    curcomb.pop()

    helper(comb,curcomb,i+1,nums,target)