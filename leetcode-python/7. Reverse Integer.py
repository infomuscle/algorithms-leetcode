# 제출 코드 - Runtime 90.54 Memory 29.42
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] != "-":
            answer = int(x[::-1])
        else:
            answer = int("-" + x[1:][::-1])

        if answer > 2 ** 31 - 1 or answer < -(2 ** 31):
            return 0

        return answer


tc1 = 123
tc2 = -123
tc3 = 120
tc4 = 1534236469

sol = Solution()
print(sol.reverse(tc1))
print(sol.reverse(tc2))
print(sol.reverse(tc3))
print(sol.reverse(tc4))
