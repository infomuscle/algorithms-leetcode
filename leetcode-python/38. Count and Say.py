# 제출 코드 - Runtime 81.33 Memory 32.08
class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        base = self.countAndSay(n - 1)

        digits = []
        digit = ""
        for i in range(len(base)):
            if i == 0:
                digit = base[i]
            else:
                if base[i] == digit[0]:
                    digit += base[i]
                else:
                    digits.append(digit)
                    digit = base[i]
        digits.append(digit)

        result = ""
        for d in digits:
            result += str(len(d)) + d[0]

        return result


sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
