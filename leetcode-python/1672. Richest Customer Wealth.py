# 제출 코드 - Runtime 98.42 Memory 61.30
class Solution:
    def maximumWealth(self, accounts):
        return max([sum(account) for account in accounts])


a1 = [[1, 2, 3], [3, 2, 1]]
a2 = [[1, 5], [7, 3], [3, 5]]
a3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

sol = Solution()
print(sol.maximumWealth(a1))
print(sol.maximumWealth(a2))
print(sol.maximumWealth(a3))
