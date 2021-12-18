# 제출 코드 - Runtime 83.99 Memory 82.37
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stock = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - stock > max_profit:
                max_profit = prices[i] - stock
            if prices[i] < stock:
                stock = prices[i]

        return max_profit


p1 = [7, 1, 5, 3, 6, 4]
p2 = [7, 6, 4, 3, 1]
p3 = [1, 2]

sol = Solution()
print(sol.maxProfit(p1))
print(sol.maxProfit(p2))
print(sol.maxProfit(p3))
