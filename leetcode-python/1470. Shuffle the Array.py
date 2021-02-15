# 제출 코드 - Runtime 99.37 Memory 92.90
class Solution:
    def shuffle(self, nums, n):
        x = nums[:n]
        y = nums[n:]

        answer = []
        for i in range(n):
            answer.append(x[i])
            answer.append(y[i])

        return answer


nums1 = [2, 5, 1, 3, 4, 7]
n1 = 3
nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
n2 = 4
nums3 = [1, 1, 2, 2]
n3 = 2

sol = Solution()
print(sol.shuffle(nums1, n1))
print(sol.shuffle(nums2, n2))
print(sol.shuffle(nums3, n3))
