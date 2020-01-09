# 제출 코드 - Runtime 86.54 Memory 34.03
from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        return len(set(count.values())) == 1


s1 = "abacbc"
s2 = "aaabb"

sol = Solution()
print(sol.areOccurrencesEqual(s1))
print(sol.areOccurrencesEqual(s2))
