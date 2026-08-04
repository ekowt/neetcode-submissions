# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        min= -sys.maxsize-1
        max = sys.maxsize

        return dfs(root,min, max)

def dfs(root, min, max):
    if root == None:
        return True
            

    if root.val <= min or root.val >= max:
        return False
        
    return dfs(root.left,min,root.val) and dfs(root.right,root.val, max)
            







        