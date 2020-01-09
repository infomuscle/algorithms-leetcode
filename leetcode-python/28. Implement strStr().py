# 제출 코드 - Runtime 87.70 Memory 34.72
class Solution:
    def strStr(self, haystack, needle):
        idx = haystack.find(needle)
        return idx


h1 = "hello"
n1 = "ll"
h2 = "aaaaa"
n2 = "bba"
h3 = "abcd"
n3 = ""
h4 = "a"
n4 = "a"

sol = Solution()
print(sol.strStr(h1, n1))
print(sol.strStr(h2, n2))
print(sol.strStr(h3, n3))
print(sol.strStr(h4, n4))
