# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive Breadth-First Search using a queue
        if not root:
            return 0
        
        level = 0
        # deque: declaring queue
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level += 1
        # time complexity O(n) traverse the whole tree once
        # space complexity O(n) height of the tree
        return level
