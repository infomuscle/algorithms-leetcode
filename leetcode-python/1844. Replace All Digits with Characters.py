# 제출 코드 - Runtime 96.34 Memory 13.79
class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            if s[i].isdigit():
                answer += chr(ord(s[i - 1]) + int(s[i]))
            else:
                answer += s[i]

        return answer


sol = Solution()

s1 = "a1c1e1"
s2 = "a1b2c3d4e"

print(sol.replaceDigits(s1))
print(sol.replaceDigits(s2))
