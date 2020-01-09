# 제출 코드 - Runtime 95.02 Memory 37.70
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = sorted(s)
        t = sorted(t)

        answer = ""
        for i in range(len(t) - 1):
            if t[i] != s[i]:
                answer = t[i]
                break
        if answer == "":
            answer = t[-1]

        return answer
