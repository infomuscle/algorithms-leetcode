# 제출 코드 - Runtime 88.11 Memory 73.71
class Solution:
    def findArray(self, pref):
        result = [pref[0]]
        for i in range(len(pref) - 1):
            result.append(pref[i] ^ pref[i + 1])

        return result


sol = Solution()

p1 = [5, 2, 0, 3, 1]
p2 = [13]

print(sol.findArray(p1))
print(sol.findArray(p2))
