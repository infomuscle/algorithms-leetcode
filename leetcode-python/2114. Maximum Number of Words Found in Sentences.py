# 제출 코드 - Runtime 98.13 Memory 87.77
class Solution:
    def mostWordsFound(self, sentences):
        return max(map(lambda s: len(s.split(" ")), sentences))


s1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
s2 = ["please wait", "continue to fight", "continue to win"]

sol = Solution()
print(sol.mostWordsFound(s1))
print(sol.mostWordsFound(s2))
