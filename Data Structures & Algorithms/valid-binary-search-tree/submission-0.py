# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[Optional[int],Optional[int],bool]:
            if node is None:
                return (None,None,True)
            leftMin,leftMax,LeftValid = dfs(node.left)
            rightMin,rightMax,rightValid = dfs(node.right)
        
            isValid = LeftValid and rightValid and(leftMax is None or node.val > leftMax) and (rightMin is None or node.val < rightMin)
            li = list(filter(lambda x: x is not None,[node.val,leftMin,rightMin,leftMax,rightMax]))

            return (min(li),max(li),isValid)
        
        minVal,maxVal,isValid = dfs(root)
        return isValid
            


