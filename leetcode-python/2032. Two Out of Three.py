# 제출 코드 - Runtime 96.52 Memory 35.98
from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        counts = defaultdict(int)

        for num in set(nums1):
            counts[num] += 1

        for num in set(nums2):
            counts[num] += 1

        for num in set(nums3):
            counts[num] += 1

        return [key for key in counts if counts[key] >= 2]
