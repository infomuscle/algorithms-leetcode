# 제출 코드 - Runtime 68.34 Memory 74.56
class Solution:
    def runningSum(self, nums):
        answer = [nums[0]]

        for i in range(1, len(nums)):
            answer.append(answer[-1] + nums[i])

        return answer


n1 = [1, 2, 3, 4]
n2 = [1, 1, 1, 1, 1]
n3 = [3, 1, 2, 10, 1]

sol = Solution()
print(sol.runningSum(n1))
print(sol.runningSum(n2))
print(sol.runningSum(n3))
