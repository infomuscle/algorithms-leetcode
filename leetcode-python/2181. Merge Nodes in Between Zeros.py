# 제출 코드 - Runtime 77.06 Memory 15.80
class Solution:
    def mergeNodes(self, head):

        merged_head = ListNode()
        merged_current = merged_head

        current = head.next
        while current.next:
            if current.val == 0:
                merged_current.next = ListNode()
                merged_current = merged_current.next
            else:
                merged_current.val += current.val
            current = current.next

        return merged_head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
