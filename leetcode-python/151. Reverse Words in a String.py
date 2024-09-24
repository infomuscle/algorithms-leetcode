# Runtime 66.15 Memory 17.77
class Solution:
    def reverseWords(self, s):

        words = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            else:
                if temp != "":
                    words.append(temp)
                    temp = ""
        if temp != "":
            words.append(temp)

        return " ".join(words[::-1])


sol = Solution()

s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"

print(sol.reverseWords(s1))
print(sol.reverseWords(s2))
print(sol.reverseWords(s3))
