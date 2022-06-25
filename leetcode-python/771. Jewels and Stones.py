# 제출 코드 - Runtime 40.00 Memory 10.89
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewel_set = set()
        for jewel in jewels:
            jewel_set.add(jewel)

        cnt = 0
        for stone in stones:
            if stone in jewel_set:
                cnt += 1

        return cnt


sol = Solution()

j1, s1 = "aA", "aAAbbbb"
j2, s2 = "z", "ZZ"

print(sol.numJewelsInStones(j1, s1))
print(sol.numJewelsInStones(j2, s2))
