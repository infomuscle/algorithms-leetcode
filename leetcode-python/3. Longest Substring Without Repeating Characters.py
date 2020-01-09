# 제출 코드 - Runtime 52.36 Memory 65.41
class Solution:
    def lengthOfLongestSubstring(self, s):

        answer = 0

        chars = []

        subs = ""
        for i, c in enumerate(s):
            if c not in chars:
                chars.append(c)
                subs += c
            else:
                subs = subs[subs.find(c) + 1:] + c
                chars = chars[chars.index(c) + 1:]
                chars.append(c)

            if len(subs) > answer:
                answer = len(subs)

        return answer


tc1 = "abcabcbb"
tc2 = "bbbbb"
tc3 = "pwwkew"
tc4 = ""
tc5 = "au"
tc6 = "dvdf"
tc7 = "  "

sol = Solution()
print(sol.lengthOfLongestSubstring(tc1))
print(sol.lengthOfLongestSubstring(tc2))
print(sol.lengthOfLongestSubstring(tc3))
print(sol.lengthOfLongestSubstring(tc4))
print(sol.lengthOfLongestSubstring(tc5))
print(sol.lengthOfLongestSubstring(tc6))
print(sol.lengthOfLongestSubstring(tc7))
