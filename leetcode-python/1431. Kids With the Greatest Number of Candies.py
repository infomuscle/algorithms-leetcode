# 제출 코드 - Runtime 82.08 Memory 94.15
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        answer = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                answer.append(True)
            else:
                answer.append(False)

        return answer


c1 = [2, 3, 5, 1, 3]
e1 = 3
c2 = [4, 2, 1, 1, 2]
e2 = 1
c3 = [12, 1, 12]
e3 = 10

sol = Solution()

print(sol.kidsWithCandies(c1, e1))
print(sol.kidsWithCandies(c2, e2))
print(sol.kidsWithCandies(c3, e3))
