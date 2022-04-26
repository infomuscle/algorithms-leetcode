# 제출 코드 - Runtime 98.01 Memory 55.07
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(s) for s in str(num)])
        return num


sol = Solution()

n1 = 38
n2 = 0
print(sol.addDigits(n1))
print(sol.addDigits(n2))
