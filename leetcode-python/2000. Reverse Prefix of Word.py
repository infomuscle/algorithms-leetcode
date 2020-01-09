# 제출 코드 - Runtime 95.02 Memory 24.97
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[i::-1] + word[i + 1:]

        return word


w1 = "abcdefd"
c1 = "d"
w2 = "xyxzxe"
c2 = "z"
w3 = "abcd"
c3 = "z"

sol = Solution()
print(sol.reversePrefix(w1, c1))
print(sol.reversePrefix(w2, c2))
print(sol.reversePrefix(w3, c3))
