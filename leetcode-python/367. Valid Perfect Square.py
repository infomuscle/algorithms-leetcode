# 제출 코드 - Runtime 27.03 Memory 56.72
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = num // 2
        while s ** 2 > num:
            s //= 2

        while s ** 2 <= num:
            if s ** 2 == num:
                return True
            s += 1

        return False


sol = Solution()

n1 = 16
n2 = 14
n3 = 35

print(sol.isPerfectSquare(n1))
print(sol.isPerfectSquare(n2))
print(sol.isPerfectSquare(n3))
