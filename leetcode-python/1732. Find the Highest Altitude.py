# 제출 코드 - Runtime 88.13 Memory 90.96
class Solution:
    def largestAltitude(self, gain):
        alts = [0]
        for g in gain:
            alts.append(alts[-1] + g)
        alts.sort()

        return alts[-1]


g1 = [-5, 1, 5, 0, -7]
g2 = [-4, -3, -2, -1, 4, 3, 2]

sol = Solution()
print(sol.largestAltitude(g1))
print(sol.largestAltitude(g2))
