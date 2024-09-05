# 제출 코드 - Runtime 94.56 Memory 51.49
class Solution:
    def coinChange(self, coins, amount):
        INF = int(1e9)

        memo = [INF] * (amount + 1)
        memo[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i - coin] + 1, memo[i])

        if memo[-1] == INF:
            return -1

        return memo[-1]


sol = Solution()

c1, a1 = [1, 2, 5], 11
c2, a2 = [2], 3
c3, a3 = [1], 0
c4, a4 = [186, 419, 83, 408], 6249
c5, a5 = [1, 2147483647], 2
print(sol.coinChange(c1, a1))
print(sol.coinChange(c2, a2))
print(sol.coinChange(c3, a3))
print(sol.coinChange(c4, a4))
print(sol.coinChange(c5, a5))
