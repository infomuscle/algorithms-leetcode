# 제출 코드 - Runtime 95.14 Memory 100
class Solution:
    temp = []
    def plusOne(self, digits):
        if digits == []:
            last = 0 + 1
        else:
            last = digits.pop() + 1
        if last >= 10:
            last -= 10
            self.temp.append(last)
            return self.plusOne(digits)
        else:
            self.temp.append(last)
            while self.temp != []:
                digits.append(self.temp.pop())
            return digits

tc1 = [1,2,3]
tc2 = [4,3,2,1]
tc3 = [9]
tc4 = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
tc5 = [4,3,5,9]

sol = Solution()
print(sol.plusOne(tc1))
print(sol.plusOne(tc2))
print(sol.plusOne(tc3))
print(sol.plusOne(tc4))
print(sol.plusOne(tc5))

# Code 1: 성공 - Runtime 95.14 Memory 100
# class Solution:
#     def plusOne(self, digits):
#         temp = []
#
#         return self.recursive(digits, temp)
#
#     def recursive(self, digits, temp):
#         if digits == []:
#             last = 0 + 1
#         else:
#             last = digits.pop() + 1
#         if last >= 10:
#             last -= 10
#             temp.append(last)
#             return self.recursive(digits, temp)
#         else:
#             temp.append(last)
#             while temp != []:
#                 digits.append(temp.pop())
#             return digits