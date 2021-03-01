# 제출 코드 - Runtime 99.85 Memory 42.98
class Solution:
    def interpret(self, command):
        mapper = {"G": "G", "()": "o", "(al)": "al"}

        answer = ""

        tmp = ""
        for c in command:
            tmp += c
            if tmp in mapper:
                answer += mapper[tmp]
                tmp = ""

        return answer


c1 = "G()(al)"
c2 = "G()()()()(al)"
c3 = "(al)G(al)()()G"

sol = Solution()
print(sol.interpret(c1))
print(sol.interpret(c2))
print(sol.interpret(c3))
