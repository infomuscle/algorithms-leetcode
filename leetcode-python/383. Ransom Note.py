# 제출 코드 - Runtime 41.69 Memory 94.38
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_map = defaultdict(int)
        for s in ransomNote:
            r_map[s] += 1

        m_map = defaultdict(int)
        for s in magazine:
            m_map[s] += 1

        for key in r_map.keys():
            if key not in m_map or r_map[key] > m_map[key]:
                return False

        return True


r1, m1 = "a", "b"
r2, m2 = "aa", "ab"
r3, m3 = "aa", "aab"

sol = Solution()
print(sol.canConstruct(r1, m1))
print(sol.canConstruct(r2, m2))
print(sol.canConstruct(r3, m3))
