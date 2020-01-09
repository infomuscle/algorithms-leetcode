# 제출 코드 - Runtime 78.56 Memory 11.45
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums):
        map = defaultdict(list)

        for i, num in enumerate(nums):
            map[num].append(i)

        answer = 0
        for key in map:
            n = len(map[key])
            if n >= 2:
                answer += (n * (n - 1)) // 2

        return answer


n1 = [1, 2, 3, 1, 1, 3]
n2 = [1, 1, 1, 1]
n3 = [1, 2, 3]

sol = Solution()
print(sol.numIdenticalPairs(n1))
print(sol.numIdenticalPairs(n2))
print(sol.numIdenticalPairs(n3))
