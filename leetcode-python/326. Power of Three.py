# 제출 코드 - Runtime 92.73 Memory 100
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False

        if n%3 == 0:
            return self.isPowerOfThree(n//3)
        else:
            return False

tc1 = 27
tc2 = 0
tc3 = 9
tc4 = 45
tc5 = 1

sol = Solution()
print(sol.isPowerOfThree(tc1))
print(sol.isPowerOfThree(tc2))
print(sol.isPowerOfThree(tc3))
print(sol.isPowerOfThree(tc4))
print(sol.isPowerOfThree(tc5))