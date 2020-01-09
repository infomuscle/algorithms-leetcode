# 제출 코드 - Runtime 82.97 Memory 89.6
class Solution:
    def sortPeople(self, names, heights):
        people = [(names[i], heights[i]) for i in range(len(names))]
        people.sort(key=lambda x: x[1], reverse=True)

        return [person[0] for person in people]
