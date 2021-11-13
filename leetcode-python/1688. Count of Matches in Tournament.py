# 제출 코드 - Runtime 96.59 Memory 35.23
class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            cnt += n // 2
            n = n // 2 + n % 2

        return cnt


n1 = 7
n2 = 14

sol = Solution()
print(sol.numberOfMatches(n1))
print(sol.numberOfMatches(n2))
