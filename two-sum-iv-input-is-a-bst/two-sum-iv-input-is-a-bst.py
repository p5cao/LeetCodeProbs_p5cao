# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # x + y = k
        # y = k - x
        T = set()
        
        def dfs(node):
            if not node:
                return False
            y = k-node.val
            if y in T:
                return True
            else:
                T.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
        