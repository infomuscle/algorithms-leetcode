# 제출 코드 - Runtime 74.42 Memory 84.05
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        distractors = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        result = 0

        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue

            front = stack.pop()
            rear = s[i]

            if front in distractors and rear in distractors[front]:
                result += romans[rear] - romans[front]
            else:
                result += romans[front]
                stack.append(rear)

        if len(stack) != 0:
            result += romans[stack.pop()]

        return result


s1 = "III"
s2 = "IV"
s3 = "IX"
s4 = "LVIII"
s5 = "MCMXCIV"

sol = Solution()

print(sol.romanToInt(s1))
print(sol.romanToInt(s2))
print(sol.romanToInt(s3))
print(sol.romanToInt(s4))
print(sol.romanToInt(s5))
