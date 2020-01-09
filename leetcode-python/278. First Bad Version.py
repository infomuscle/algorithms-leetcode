# 제출 코드 - Runtime 50.37 Memory 12.57
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        mid = (l + r) // 2
        while l <= r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1
        return mid


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(n):
    return True
