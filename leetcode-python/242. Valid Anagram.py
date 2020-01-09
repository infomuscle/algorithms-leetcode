# 제출 코드 - Runtime 92.69 Memory 81.22
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1

        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1

        return s_map == t_map


s1, t1 = "anagram", "nagaram"
s2, t2 = "rat", "car"

sol = Solution()
print(sol.isAnagram(s1, t1))
print(sol.isAnagram(s2, t2))
