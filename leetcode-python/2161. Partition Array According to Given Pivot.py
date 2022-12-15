# 제출 코드 - Runtime 85.59 Memory 11.15
class Solution:
    def pivotArray(self, nums, pivot: int):
        left, right, pivots = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                pivots.append(num)

        return left + pivots + right
