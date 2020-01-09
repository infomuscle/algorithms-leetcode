# 제출 코드 - Runtime 54.71 Memory 88.54
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


a1 = "1.1.1.1"
a2 = "255.100.50.0"

sol = Solution()
print(sol.defangIPaddr(a1))
print(sol.defangIPaddr(a2))
