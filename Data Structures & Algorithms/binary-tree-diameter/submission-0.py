# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        def dfs(node:Optional[TreeNode])->int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter[0] = max(
                maxDiameter[0], 
                1+(left+right)
            )

            return 1+max(left, right)
        
        dfs(root)
        return maxDiameter[0]-1
            