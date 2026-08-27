"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyHead = Node(0)
        dummyTail = dummyHead
        # 元のnodeからコピーnodeへの参照変換のため
        originToNew = {}

        while head:
            tmp = head.next
            new_node = Node(head.val, None, head.random)
            originToNew[head] = new_node
            dummyTail.next = new_node
            dummyTail = dummyTail.next 
            head = tmp
        
        dummyTail = dummyHead
        while dummyTail:
            dummyTail.random = originToNew[dummyTail.random] if dummyTail.random else None
            dummyTail = dummyTail.next
        
        return dummyHead.next
