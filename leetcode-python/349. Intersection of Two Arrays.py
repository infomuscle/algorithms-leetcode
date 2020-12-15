# 제출 코드 - Runtime 30.38 Memory 93.54
class Solution:
    def intersection(self, nums1, nums2):
        numsMain = []
        numsCompare = []
        answer = []
        if len(nums1) < len(nums2):
            numsMain = nums1
            numsCompare = nums2
        else:
            numsMain = nums2
            numsCompare = nums1

        for i in range(len(numsMain)):
            if numsMain[i] in numsCompare and numsMain[i] not in answer:
                answer.append(numsMain[i])

        return answer


sol = Solution()
n11 = [1, 2, 2, 1]
n12 = [2, 2]
n21 = [4, 9, 5]
n22 = [9, 4, 9, 8, 4]

print(sol.intersection(n11, n12))
print(sol.intersection(n21, n22))
