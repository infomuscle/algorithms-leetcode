# 제출 코드 - Runtime 80.13 Memory 18.50
class Solution:
    def hasCycle(self, head) -> bool:
        visited = set()

        e = head
        while e:
            if e in visited:
                return True
            visited.add(e)
            e = e.next

        return False


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
