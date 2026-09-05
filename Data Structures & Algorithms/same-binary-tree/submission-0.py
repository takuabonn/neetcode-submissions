# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_p:Optional[TreeNode], node_q:Optional[TreeNode]) -> bool:
            if not node_p and not node_q:
                return True
            elif None in [node_p, node_q]:
                return False
            
            if node_p.val != node_q.val:
                return False
            
            left = dfs(node_p.left, node_q.left)
            right = dfs(node_p.right, node_q.right)

            return left and right
            
        return dfs(p, q)
