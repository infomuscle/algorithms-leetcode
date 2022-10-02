# 제출 코드 - Runtime 33.71 Memory 26.56
from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        line = defaultdict(list)
        way = -1

        current = 0
        for c in s:
            line[current].append(c)
            if current == 0:
                way *= -1
            elif current % ((2 * numRows) - 2) + 1 == numRows:
                way *= - 1

            current += 1 * way

        return "".join(["".join(line[i]) for i in range(numRows)])


sol = Solution()

s1 = "PAYPALISHIRING"
n1 = 3
s2 = "PAYPALISHIRING"
n2 = 4
s3 = "A"
n3 = 1
s4 = "AB"
n4 = 1

print(sol.convert(s1, n1))
print(sol.convert(s2, n2))
print(sol.convert(s3, n3))
print(sol.convert(s4, n4))

# 3
# 0 4 8 12
# 1 3 5 7 9 11 13
# 2 6 10 14


# 4
# 0 6 12
# 1 5 7 11 13
# 2 4 8 10
# 3 9 15


# (2* numRows -2)
# (numRows - 1)
# i% ((2* numRows) - 2) + 1 == numrows

# 5
# 0
# 1
