# 제출 코드 - Runtime 72.47 Memory 83.80
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")

        dictionary = {}
        idx = 0
        for k in key:
            if k not in dictionary:
                dictionary[k] = ord("a") + idx
                idx += 1

        return "".join([chr(dictionary[m]) if m != " " else m for m in message])


sol = Solution()

k1 = "the quick brown fox jumps over the lazy dog"
m1 = "vkbs bs t suepuv"
k2 = "eljuxhpwnyrdgtqkviszcfmabo"
m2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

print(sol.decodeMessage(k1, m1))
print(sol.decodeMessage(k2, m2))
