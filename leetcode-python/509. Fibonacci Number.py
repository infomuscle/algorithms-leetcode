# 제출 코드 - Runtime 13.63 Memory 73.96
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


sol = Solution()

print(sol.fib(2))
print(sol.fib(3))
print(sol.fib(4))
print(sol.fib(5))
print(sol.fib(6))
print(sol.fib(7))
