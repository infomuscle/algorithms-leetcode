# 제출 코드 - Runtime 48.11 Memory 57.22
class Solution:
    def countConsistentStrings(self, allowed, words):
        return len(list(filter(lambda word: len({w for w in word} - {c for c in allowed}) == 0, words)))


sol = Solution()

a1 = "ab"
w1 = ["ad", "bd", "aaab", "baa", "badab"]
a2 = "abc"
w2 = ["a", "b", "c", "ab", "ac", "bc", "abc"]
a3 = "cad"
w3 = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]

print(sol.countConsistentStrings(a1, w1))
print(sol.countConsistentStrings(a2, w2))
print(sol.countConsistentStrings(a3, w3))
