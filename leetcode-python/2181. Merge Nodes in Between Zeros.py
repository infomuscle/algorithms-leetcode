# 제출 코드 - Runtime 91.14 Memory 41.6
class Solution:
    def mergeNodes(self, head):

        result = []

        current_node = head.next
        merged = 0
        while current_node:
            if current_node.val == 0:
                result.append(merged)
                merged = 0
            merged += current_node.val
            current_node = current_node.next

        new_head = ListNode(result[0], None)
        current = new_head
        for i in range(1, len(result)):
            current.next = ListNode(result[i], None)
            current = current.next

        return new_head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
