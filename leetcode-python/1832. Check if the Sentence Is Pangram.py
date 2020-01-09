# 제출 코드 - Runtime 56.49 Memory 12.61
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([c for c in sentence])) == 26


sol = Solution()

s1 = "thequickbrownfoxjumpsoverthelazydog"
s2 = "leetcode"

print(sol.checkIfPangram(s1))
print(sol.checkIfPangram(s2))
