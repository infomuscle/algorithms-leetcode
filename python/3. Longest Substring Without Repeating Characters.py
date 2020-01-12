class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 1
        longest = ""

        if s == "":
            return len(s)

        temp = ""
        while True:
            if len(temp) == 0:
                temp += s[left]
            else:
                if s[right] not in temp:
                    temp += s[right]
                    right += 1
                else:
                    while s[left] != s[right]:
                        left += 1
                    left += 1
                    temp = ""


            if len(temp) > len(longest):
                longest = temp
            print("temp: " + temp + "   longest: " +longest + "   left: " + str(left) + "   right: " + str(right))
            if len(s) == right:
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
# print(sol.lengthOfLongestSubstring(tc1))
# print(sol.lengthOfLongestSubstring(tc2))
# print(sol.lengthOfLongestSubstring(tc3))
# print(sol.lengthOfLongestSubstring(tc4))
# print(sol.lengthOfLongestSubstring(tc5))
# print(sol.lengthOfLongestSubstring(tc6))
# print(sol.lengthOfLongestSubstring(tc7))
sol.lengthOfLongestSubstring(tc3)
# sol.lengthOfLongestSubstring(tc4)
# sol.lengthOfLongestSubstring(tc5)
# sol.lengthOfLongestSubstring(tc6)
# sol.lengthOfLongestSubstring(tc7)

