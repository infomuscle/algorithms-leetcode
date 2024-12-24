# 제출 코드 - Runtime 97.92 Memory 44.20
class Solution:
    def productExceptSelf(self, nums):

        zeros = 0
        product = 1
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1

        result = []
        for num in nums:
            if num == 0:
                if zeros == 1:
                    result.append(product)
                else:
                    result.append(0)
            else:
                if zeros > 0:
                    result.append(0)
                else:
                    result.append(product // num)

        return result


sol = Solution()

n1 = [1, 2, 3, 4]
n2 = [-1, 1, 0, -3, 3]

print(sol.productExceptSelf(n1))
print(sol.productExceptSelf(n2))
