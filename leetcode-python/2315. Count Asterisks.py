# 제출 코드 - Runtime 58.41 Memory 11.10
class Solution:
    def countAsterisks(self, s: str) -> int:

        stack = []

        asterisks = 0
        for c in s:
            if c == "|":
                if len(stack) == 0:
                    stack.append(c)
                else:
                    stack = []
                continue
            if len(stack) == 0:
                if c == "*":
                    asterisks += 1

        return asterisks
