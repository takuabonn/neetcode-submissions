# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        dq = deque([(root.val, root)])
        count = 0
        while dq:
            nextList = []
            for curMaxVal,node in dq:
                if node.val >= curMaxVal:
                    count = count + 1
                
                if node.left:
                    nextList.append((max(node.val, curMaxVal), node.left))
                if node.right:
                    nextList.append((max(node.val, curMaxVal), node.right))
            
            dq = deque(nextList)
        
        return count
                



                
                
                






        