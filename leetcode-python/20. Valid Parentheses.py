# 제출 코드 - Runtime 56.32 Memory 40.74
class Solution:
    def isValid(self, s: str) -> bool:

        match = {")": "(", "}": "{", "]": "["}

        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
                continue

            if len(stack) != 0 and stack[-1] == match[c]:
                stack.pop()
            else:
                return False

        if (len(stack) != 0):
            return False

        return True


sol = Solution()

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"

print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))
print(sol.isValid(s4))
print(sol.isValid(s5))
