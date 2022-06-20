# 제출 코드 - Runtime 71.34 Memory 57.77
from collections import deque


class Solution:
    perms = []

    def permute(self, nums):
        self.perms = []

        self.permutation(deque(nums), [])
        return self.perms

    def permutation(self, nums_left, perm):
        if len(nums_left) == 0:
            self.perms.append(perm)
            return perm

        result = []
        for i in range(len(nums_left)):
            num = nums_left.popleft()
            self.permutation(nums_left, perm + [num])
            nums_left.append(num)

        return result


sol = Solution()
n1 = [1, 2, 3]
n2 = [0, 1]

print(sol.permute(n1))
print(sol.permute(n2))

#      (1)                (2)           (3)
# (1,2) (1,3)         (2,1) (2,3)   (3,1) (3,2)
# (1,2,3) (1,3,2)
