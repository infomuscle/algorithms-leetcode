# 제출 코드 - Runtime 60.63 Memory 11.10
class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisks = 0
        flag = False
        for c in s:
            if c == "|":
                flag = not flag
                continue
            if not flag and c == "*":
                asterisks += 1

        return asterisks
