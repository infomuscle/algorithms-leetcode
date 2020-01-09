# 제출 코드 - Runtime 99.94 Memory 67.93
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)
        return bits.count("1")


n1 = int("00000000000000000000000000001011", 2)
n2 = int("00000000000000000000000010000000", 2)
n3 = int("11111111111111111111111111111101", 2)

sol = Solution()
print(sol.hammingWeight(n1))
print(sol.hammingWeight(n2))
print(sol.hammingWeight(n3))
