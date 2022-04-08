# 제출 코드 - Runtime 67.92 Memory 57.14
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n % 2 == 0 and n >= 1:
            n = n / 2
            if n == 1:
                return True
        return False


sol = Solution()
n1 = 1
n2 = 16
n3 = 3

print(sol.isPowerOfTwo(n1))
print(sol.isPowerOfTwo(n2))
print(sol.isPowerOfTwo(n3))
