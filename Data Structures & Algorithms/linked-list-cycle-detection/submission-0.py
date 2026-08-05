# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        while head:
            node_set.add(head)
            if head.next in node_set:
                return True
            head = head.next

        return False