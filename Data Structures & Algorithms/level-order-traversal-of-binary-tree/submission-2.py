# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if not root:
            return []
        q.append(root)
        rit = []
        while q:
            res = []
            for i in range(len(q)):
                cur = q.popleft()
                res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            rit.append(res)
        
        return rit
            

        