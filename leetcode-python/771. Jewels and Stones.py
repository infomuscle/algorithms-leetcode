# 제출 코드 - Runtime 56.93 Memory 10.89
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return len(list(filter(lambda x: x in jewel_set, stones)))


sol = Solution()

j1, s1 = "aA", "aAAbbbb"
j2, s2 = "z", "ZZ"

print(sol.numJewelsInStones(j1, s1))
print(sol.numJewelsInStones(j2, s2))
