# 제출 코드 - Runtime 99.32 Memory 100
class Solution:
    def reverseString(self, s):
        s.reverse()
        print(s)
        # s.reverse()


sample1 = ["h","e","l","l","o"]
sample2 = ["H","a","n","n","a","h"]

sol = Solution()
sol.reverseString(sample1)
sol.reverseString(sample2)

# reverser(sample1)
# reverser(sample2)


### Code 1 - 성공
# def reverser(l):
#     for i in range(len(l)-1):
#         l.insert(i, l.pop())
#     print(l)