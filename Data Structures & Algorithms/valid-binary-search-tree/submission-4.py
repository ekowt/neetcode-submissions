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

        return dfs(root,mini,maxi)

def dfs(root,mini,maxi):
    if not root:
        return True

    if root.val <= mini or  root.val >= maxi:
        return False

    return dfs(root.left,mini,root.val) and dfs(root.right,root.val,maxi)
