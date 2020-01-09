# 제출 코드 - Runtime 65.57 Memory 91.22
class Solution:
    def average(self, salary):
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


s1 = [4000, 3000, 1000, 2000]
s2 = [1000, 2000, 3000]
s3 = [6000, 5000, 4000, 3000, 2000, 1000]
s4 = [8000, 9000, 2000, 3000, 6000, 1000]

sol = Solution()
print(sol.average(s1))
print(sol.average(s2))
print(sol.average(s3))
print(sol.average(s4))
