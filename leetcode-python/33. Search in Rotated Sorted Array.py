# 제출 코드 - Runtime 100.00 Memory 17.77
class Solution:
    def search(self, nums, target):
        return self.search_split(nums, target, 0, len(nums) - 1)

    def search_split(self, nums, target, start, end):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return start
            else:
                return -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return start + mid

        previous = self.search_split(nums[:mid], target, start, start + mid - 1)
        next = self.search_split(nums[mid + 1:], target, start + mid + 1, end)

        return max(previous, next)


sol = Solution()

n1, t1 = [4, 5, 6, 7, 0, 1, 2], 0
n2, t2 = [4, 5, 6, 7, 0, 1, 2], 3
n3, t3 = [1], 0
n4, t4 = [1, 3], 3
n5, t5 = [4, 5, 6, 7, 0, 1, 2], 2

print(sol.search(n1, t1))
print(sol.search(n2, t2))
print(sol.search(n3, t3))
print(sol.search(n4, t4))
print(sol.search(n5, t5))
