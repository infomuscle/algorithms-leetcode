# 제출 코드 - Runtime 95.61 Memory 13.79
class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            if s[i].isdigit():
                answer += self.shift(s[i - 1], int(s[i]))
            else:
                answer += s[i]

        return answer

    def shift(self, c, x):
        return chr(ord(c) + x)


sol = Solution()

s1 = "a1c1e1"
s2 = "a1b2c3d4e"

print(sol.replaceDigits(s1))
print(sol.replaceDigits(s2))
