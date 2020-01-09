# 제출 코드 - Runtime 98.55 Memory 62.39
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 is not None or l2 is not None:
            if l2 is None or (l1 is not None and l1.val <= l2.val):
                current.next = l1
                l1 = l1.next
            elif l1 is None or (l2 is not None and l1.val > l2.val):
                current.next = l2
                l2 = l2.next
            current = current.next

        return dummy.next
