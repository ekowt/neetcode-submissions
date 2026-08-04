# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        dia = left+right
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(dia,sub)

    

    def depth(self,root):

        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        return 1+max(left,right)
        