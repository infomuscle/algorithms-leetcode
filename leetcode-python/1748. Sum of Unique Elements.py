# 제출 코드 - Runtime 96.29 Memory 76.04
class Solution:
    def sumOfUnique(self, nums):

        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1

        answer = 0
        for key in map:
            if map[key] == 1:
                answer += key

        return answer


n1 = [1, 2, 3, 2]
n2 = [1, 1, 1, 1, 1]
n3 = [1, 2, 3, 4, 5]

sol = Solution()

print(sol.sumOfUnique(n1))
print(sol.sumOfUnique(n2))
print(sol.sumOfUnique(n3))
