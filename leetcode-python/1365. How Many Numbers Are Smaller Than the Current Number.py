# 제출 코드 - Runtime 89.45 Memory 14.28
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        map = dict()
        for i, num in enumerate(sorted_nums):
            if num not in map:
                map[num] = i

        return [map[num] for num in nums]


n1 = [8, 1, 2, 2, 3]
n2 = [6, 5, 4, 8]
n3 = [7, 7, 7, 7]

sol = Solution()
print(sol.smallerNumbersThanCurrent(n1))
print(sol.smallerNumbersThanCurrent(n2))
print(sol.smallerNumbersThanCurrent(n3))
