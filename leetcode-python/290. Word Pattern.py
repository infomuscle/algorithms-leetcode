# 제출 코드 - Runtime 76.09 Memory 78.87
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = dict()

        p_list = [p for p in pattern]
        s_list = s.split()

        if len(p_list) != len(s_list) or len(set(p_list)) != len(set(s_list)):
            return False

        for i, p in enumerate(p_list):
            p_map[p] = s_list[i]
        for i, p in enumerate(pattern):
            if p_map[p] != s_list[i]:
                return False

        return True


p1 = "abba"
s1 = "dog cat cat dog"
p2 = "abba"
s2 = "dog cat cat fish"
p3 = "aaaa"
s3 = "dog cat cat dog"
p4 = "abba"
s4 = "dog dog dog dog"
p5 = "aba"
s5 = "cat cat cat dog"

sol = Solution()
print(sol.wordPattern(p1, s1))
print(sol.wordPattern(p2, s2))
print(sol.wordPattern(p3, s3))
print(sol.wordPattern(p4, s4))
print(sol.wordPattern(p5, s5))
