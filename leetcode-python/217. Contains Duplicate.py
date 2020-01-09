# 제출 코드 - Runtime 69.38 Memory 11.25
class Solution:
    def containsDuplicate(self, nums):
        isIn = dict()
        for num in nums:
            if num in isIn:
                return True
            isIn[num] = True
        return False


sol = Solution()

l1 = [1, 2, 3, 1]
l2 = [1, 2, 3, 4]
l3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
l4 = []

print(sol.containsDuplicate(l1))
print(sol.containsDuplicate(l2))
print(sol.containsDuplicate(l3))
print(sol.containsDuplicate(l4))
