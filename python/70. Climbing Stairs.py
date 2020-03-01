# 제출 코드 - Runtime 96.48 Memory 98.51
class Solution:
    def climbStairs(self, n: int):
        answer = 0

        for i in range(int(n/2)+1):
           answer += self.nCk(n-i, i)

        return answer

    def nCk(self, n, k):
        upper = 1
        lower = 1
        for i in range(k):
            upper *= n - i
            lower *= k - i

        return int(upper/lower)



sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(4))
print(sol.climbStairs(5))
print(sol.climbStairs(6))
