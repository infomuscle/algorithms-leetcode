# 제출 코드 - Runtime 96.47 Memory 27.11
class Solution:
    def restoreString(self, s, indices):
        map = {}
        for i, idx in enumerate(indices):
            map[idx] = s[i]

        return "".join([map[i] for i in range(len(indices))])


sol = Solution()

s1 = "codeleet"
i1 = [4, 5, 6, 7, 0, 2, 1, 3]
s2 = "abc"
i2 = [0, 1, 2]

print(sol.restoreString(s1, i1))
print(sol.restoreString(s2, i2))
