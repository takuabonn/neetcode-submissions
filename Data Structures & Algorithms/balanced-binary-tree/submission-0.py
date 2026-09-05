# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode]) -> tuple[int,bool]:
            if not node:
                return (0,True)
            
            leftH,leftBalance = dfs(node.left)
            rightH,rightBalance = dfs(node.right)
            if not leftBalance or not rightBalance:
                return (0, False)
            
            diff = abs(leftH - rightH)
            return (1+max(leftH, rightH), diff <= 1)
        
        h,balanced = dfs(root)
        return balanced
        

            
            

            

            