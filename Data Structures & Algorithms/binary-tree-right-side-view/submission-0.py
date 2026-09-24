# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []
        while True:
            mostRight = None
            tmp = []
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                if not mostRight:
                    mostRight = node
                tmp.append(node.right)
                tmp.append(node.left)

            if mostRight:
                result.append(mostRight.val)
            if not tmp:
                return result
            queue = deque(tmp)
            


                
                
                


                
                

        