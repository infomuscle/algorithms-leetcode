# 제출 코드 - Runtime 67.01 Memory 93.18
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = ""

        len_open, len_close = 0, 0
        temp = ""
        for c in s:
            if c == "(":
                temp += c
                len_open += 1
            else:
                temp += c
                len_close += 1
                if len_open == len_close:
                    answer += temp[1: len(temp) - 1]
                    temp = ""

        return answer


sol = Solution()

s1 = "(()())(())"
s2 = "(()())(())(()(()))"
s3 = "()()"

print(sol.removeOuterParentheses(s1))
print(sol.removeOuterParentheses(s2))
print(sol.removeOuterParentheses(s3))
