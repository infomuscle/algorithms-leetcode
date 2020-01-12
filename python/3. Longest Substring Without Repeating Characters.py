class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        longest = ""

        if s == "":
            return len(s)

        temp = ""
        while True:
            if s[right] not in temp:
                temp += s[right]
                right += 1
            else:
                while True:
                    if s[left] == s[right]:
                        left += 1
                    else:
                        left -= 1
                        break
                temp = s[left:right+1]
            if len(temp) > len(longest):
                longest = temp
            if right == len(s):
                break

        return len(longest)


tc1 = "abcabcbb"
tc2 = "bbbbb"
tc3 = "pwwkew"
tc4 = ""
tc5 = " "
tc6 = "au"
tc7 = "dvdf"

sol = Solution()
print(sol.lengthOfLongestSubstring(tc1))
# print(sol.lengthOfLongestSubstring(tc2))
# print(sol.lengthOfLongestSubstring(tc3))
# print(sol.lengthOfLongestSubstring(tc4))
# print(sol.lengthOfLongestSubstring(tc5))
# print(sol.lengthOfLongestSubstring(tc6))
# print(sol.lengthOfLongestSubstring(tc7))
# sol.lengthOfLongestSubstring(tc3)
# sol.lengthOfLongestSubstring(tc4)
# sol.lengthOfLongestSubstring(tc5)
# sol.lengthOfLongestSubstring(tc6)
# sol.lengthOfLongestSubstring(tc7)

