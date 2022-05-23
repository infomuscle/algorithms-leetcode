# 제출 코드 - Runtime 32.49 Memory 28.55
class Solution:
    def reverseList(self, head):
        if not head:
            return head

        map = dict()

        node = head
        while node.next:
            map[node.next] = node
            node = node.next

        head = node
        while node in map:
            node.next = map[node]
            node = node.next
        node.next = None

        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
