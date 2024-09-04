# 제출 코드 - Runtime 93.92 Memory 64.53
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s):

        letter_count = defaultdict(int)
        for c in s:
            letter_count[c] += 1

        letter_length = 0
        add_one_more = False
        for key in letter_count:
            letter_length += letter_count[key]
            if letter_count[key] % 2 != 0:
                letter_length -= 1
                add_one_more = True
        if add_one_more:
            letter_length += 1

        return letter_length


sol = Solution()

s1 = "abccccdd"
s2 = "a"

print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
