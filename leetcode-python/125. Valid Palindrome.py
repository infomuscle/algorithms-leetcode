# 제출 코드 - Runtime 98.74 Memory 37.44
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(list(filter(str.isalnum, s))).lower()
        p_s, p_e = 0, len(filtered) - 1
        while p_s < p_e:
            if filtered[p_s] != filtered[p_e]:
                return False
            p_s += 1
            p_e -= 1
        return True
