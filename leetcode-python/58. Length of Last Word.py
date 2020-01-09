# 제출 코드 - Runtime 96.26 Memory 100
class Solution:
    def lengthOfLastWord(self, s: str):
        s = s.strip()
        strList = s.split(" ")

        try:
            return len(strList.pop())
        except:
            return 0




sol = Solution()
print(sol.lengthOfLastWord(" a "))