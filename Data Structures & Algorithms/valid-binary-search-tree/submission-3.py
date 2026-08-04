# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxi = sys.maxsize
        mini = -1*(sys.maxsize-1)

        return dfs(root,maxi,mini)
         

def dfs(root,maxi,mini):
    if not root:
        return True
    
    if root.val <= mini or root.val>= maxi:
        return False
    
    return dfs(root.left,root.val,mini) and dfs(root.right,maxi,root.val)