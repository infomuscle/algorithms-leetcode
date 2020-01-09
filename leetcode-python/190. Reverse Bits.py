# 제출 코드 - Runtime 99.50 Memory 67.54
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = bin(n)[2:].zfill(32)[::-1]
        return int(reversed_bits, 2)


n1 = int("00000010100101000001111010011100", 2)
n2 = int("11111111111111111111111111111101", 2)

sol = Solution()
print(sol.reverseBits(n1))
print(sol.reverseBits(n2))
