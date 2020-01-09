# 제출 코드 - Runtime 85.36 Memory 98.41
class Solution:
    def partition(self, head, x: int):
        if not head:
            return head
        partition1, head1 = None, None
        partition2, head2 = None, None

        current = head
        while current:
            if current.val < x:
                if not head1:
                    head1 = current
                    partition1 = current
                else:
                    partition1.next = current
                    partition1 = partition1.next
            else:
                if not head2:
                    head2 = current
                    partition2 = current
                else:
                    partition2.next = current
                    partition2 = partition2.next
            current = current.next
        if partition1:
            partition1.next = head2
        if partition2:
            partition2.next = None

        return head1 if head1 else head2


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
