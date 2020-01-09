# 제출 코드 - Runtime 72.69 Memory 97.7
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')


sol = Solution()

a1 = "11"
b1 = "1"
a2 = "1010"
b2 = "1011"

print(sol.addBinary(a1, b1))
print(sol.addBinary(a2, b2))
