# 제출 코드 - Runtime 87.69 Memory 29.27
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


s1 = "Hello how are you Contestant"
k1 = 4
s2 = "What is the solution to this problem"
k2 = 4
s3 = "chopper is not a tanuki"
k3 = 5

sol = Solution()
print(sol.truncateSentence(s1, k1))
print(sol.truncateSentence(s2, k2))
print(sol.truncateSentence(s3, k3))
