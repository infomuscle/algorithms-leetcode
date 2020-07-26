# 제출 코드 - Runtime 29.64 Memory 5.11
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0

        x = str(x)
        if x[0] != "-":
            answer = x[::-1]

        else:
            answer = "-" + x[1:][::-1]

        if int(answer) > 2 ** 31 - 1 or int(answer) < -(2 ** 31):
            return 0

        return int(answer)


tc1 = 123
tc2 = -123
tc3 = 120
tc4 = 1534236469

sol = Solution()
print(sol.reverse(tc1))
print(sol.reverse(tc2))
print(sol.reverse(tc3))
print(sol.reverse(tc4))
print(tc4)
print(2**31-1)

