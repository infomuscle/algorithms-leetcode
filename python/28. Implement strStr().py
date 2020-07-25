# 제출 코드 - Runtime 72.42 Memory 15.14
class Solution:
    def strStr(self, haystack, needle):

        if len(needle) == 0:
            return 0

        idx = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                idx = i
                break

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
