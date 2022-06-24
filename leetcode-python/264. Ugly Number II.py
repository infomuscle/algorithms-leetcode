# 제출 코드 - Runtime 5.22 Memory 7.11
class Solution:
    multipliers = [2, 3, 5]

    def nthUglyNumber(self, n: int) -> int:
        return self.uglys({1}, n)[n - 1]

    def uglys(self, current, n):
        if len(current) > n:
            return sorted(list(current))

        new = current.copy()
        max_num = max(new) * 5
        for num in current:
            for multiplier in self.multipliers:
                t = num
                while t * multiplier <= max_num:
                    new.add(t * multiplier)
                    t *= multiplier
                max_num = max(max_num, t)

        return self.uglys(new, n)


sol = Solution()

n1 = 10
n2 = 1
n3 = 103
n4 = 1690
n5 = 1447

print(sol.nthUglyNumber(n1))
print(sol.nthUglyNumber(n2))
print(sol.nthUglyNumber(n3))
print(sol.nthUglyNumber(n4))
print(sol.nthUglyNumber(n5))
