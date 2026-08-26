# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 要素数を数える
        size = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            size = size + 1

        # 前方からの位置
        targetIndex = size - n

        # dumyHeadとdumyTailを定義
        # 対象位置までdumyHeadに現在のheadのnodeを連結させる
        # dumyTailのポインタを移動していく
        index = 0
        dumyHead = ListNode()
        dumyTail = dumyHead
        while index < targetIndex:
            tmp = head.next
            head.next = None
            dumyTail.next = head
            dumyTail = dumyTail.next
            head = tmp
            index = index + 1
        
        # 現状のheadは削除対象になっている
        # head.nextをdumyTail.nextに代入
        dumyTail.next = head.next

        # 最後にdumyHead.nextを返す
        return dumyHead.next

        

        
        
