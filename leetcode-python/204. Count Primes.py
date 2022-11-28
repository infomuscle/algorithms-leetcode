# 제출 코드 - Runtime 76.42 Memory 84.52
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, n, i):
                    primes[j] = False

        return sum(primes)


sol = Solution()

n1 = 10
n2 = 0
n3 = 1
n4 = 2
n5 = 5000000

print(sol.countPrimes(n1))
print(sol.countPrimes(n2))
print(sol.countPrimes(n3))
print(sol.countPrimes(n4))
print(sol.countPrimes(n5))
