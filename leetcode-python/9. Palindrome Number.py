# 제출 코드 - Runtime 97.24 Memory 23.01
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        pal = x[::-1]
        if pal == x:
            return True
        else:
            return False


tc1 = 121
tc2 = -121
tc3 = 10

sol = Solution()
print(sol.isPalindrome(tc1))
print(sol.isPalindrome(tc2))
print(sol.isPalindrome(tc3))
