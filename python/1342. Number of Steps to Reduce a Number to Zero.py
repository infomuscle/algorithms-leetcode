# 제출 코드 - Runtime 85.76 Memory 100
class Solution:
    def numberOfSteps(self, num: int):
        step = 0

        while num != 0:
            if num%2 == 0:
                num /= 2
            else:
                num -= 1
            step += 1

        return step


sol = Solution()

print(sol.numberOfSteps(14))
print(sol.numberOfSteps(8))
print(sol.numberOfSteps(123))
