# 제출 코드 - Runtime 97.39 Memory 73.42
class Solution:
    def prefixCount(self, words, pref):
        return len(list(filter(lambda word: word[:len(pref)] == pref, words)))


w1 = ["pay", "attention", "practice", "attend"]
p1 = "at"
w2 = ["leetcode", "win", "loops", "success"]
p2 = "cod"

sol = Solution()
print(sol.prefixCount(w1, p1))
print(sol.prefixCount(w2, p2))
