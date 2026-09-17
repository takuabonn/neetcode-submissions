# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])

        while True:
            stack = []
            tmp = deque()
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                stack.append(node.val)
                tmp.append(node.left)
                tmp.append(node.right)
                
            if stack:
                result.append(stack)
            
            queue = tmp
            if not queue:
                return result

            


        



                

        
