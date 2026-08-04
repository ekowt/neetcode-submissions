class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

    helper(i+1,nums,cur,res)