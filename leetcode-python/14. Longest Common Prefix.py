# 제출 코드 - Runtime 95.37 Memory 81.55
class Solution:
    def longestCommonPrefix(self, strs):

        prefix = ""
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for s in strs:
                if s[:i + 1] != prefix:
                    return prefix[:-1]

        return prefix


s1 = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]

sol = Solution()
print(sol.longestCommonPrefix(s1))
print(sol.longestCommonPrefix(s2))
