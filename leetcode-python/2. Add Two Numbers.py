# 제출 코드 - Runtime 97.43 Memory 44.76
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        value = l1.val + l2.val
        current = ListNode(value % 10, None)
        adder = value // 10

        start = current

        while (l1.next is not None or l2.next is not None) or adder != 0:
            if l1.next is None:
                l1.next = ListNode()
            if l2.next is None:
                l2.next = ListNode()

            value = l1.next.val + l2.next.val + adder
            current.next = ListNode(value % 10, None)
            adder = value // 10

            l1, l2, current = l1.next, l2.next, current.next

            if l1.next is None and l2.next is None and adder != 0:
                current.next = ListNode(adder, None)
                break

        return start
