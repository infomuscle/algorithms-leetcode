# 제출 코드 - Runtime 53.44 Memory 56.29
class Solution:
    def reverseList(self, head):
        if not head:
            return head

        next_node = head.next
        node = head
        head.next = None
        while next_node:
            next_next_node = next_node.next
            next_node.next = node
            node = next_node
            next_node = next_next_node

        return node


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
