# 제출 코드 - Runtime 90.10 Memory 57.81

class Solution:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        position = intervals.index(newInterval)

        merge_start_index = position
        for i in range(position, -1, -1):
            if not self.can_be_merged(intervals[position], intervals[i]):
                break
            merge_start_index = i

        merge_end_index = position
        for i in range(position, len(intervals)):
            if not self.can_be_merged(intervals[position], intervals[i]):
                break
            merge_end_index = i

        merged = self.merge(intervals[position], intervals[merge_start_index])
        merged = self.merge(merged, intervals[merge_end_index])

        return intervals[:merge_start_index] + [merged] + intervals[merge_end_index + 1:]

    def can_be_merged(self, interval1, interval2):
        intervals = sorted([interval1, interval2], key=lambda x: x[0])

        return not (intervals[0][1] < intervals[1][0])

    def merge(self, interval1, interval2):
        intervals = sorted([interval1, interval2], key=lambda x: x[0])

        return [min(intervals[0][0], intervals[1][0]), max(intervals[0][1], intervals[1][1])]


sol = Solution()

i1, n1 = [[1, 3], [6, 9]], [2, 5]  # 앞 병합
i2, n2 = [[1, 3], [6, 9]], [5, 6]  # 뒤 병합
i3, n3 = [[1, 3], [6, 9]], [3, 6]  # 앞뒤 병합
i4, n4 = [[1, 3], [6, 9]], [4, 5]  # 인서트
i5, n5 = [], [4, 5]  # 인서트
i6, n6 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]  # 앞 뒤 병합
i7, n7 = [[1, 3]], [4, 5]  # 인서트
i8, n8 = [[1, 6]], [2, 3]  # 병합
i9, n9 = [[1, 5]], [1, 7]  # 병합
print(sol.insert(i1, n1))
print(sol.insert(i2, n2))
print(sol.insert(i3, n3))
print(sol.insert(i4, n4))
print(sol.insert(i5, n5))
print(sol.insert(i6, n6))
print(sol.insert(i7, n7))
print(sol.insert(i8, n8))
print(sol.insert(i9, n9))
