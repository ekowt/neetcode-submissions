class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,cur = [],[]
        helper(0,nums,cur,res)
        return res

def helper(i,nums,cur,res):
    if i == len(nums):
        res.append(cur.copy())
        return
    
    cur.append(nums[i])
    helper(i+1,nums,cur,res)
    cur.pop()

    while i+1<len(nums) and nums[i] == nums[i+1]:
        i+=1
    helper(i+1,nums,cur,res)