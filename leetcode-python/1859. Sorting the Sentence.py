# 제출 코드 - Runtime 95.01 Memory 76.83
class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([c[:-1] for c in sorted(s.split(), key=lambda x: x[-1])])


s1 = "is2 sentence4 This1 a3"

sol = Solution()
print(sol.sortSentence(s1))
