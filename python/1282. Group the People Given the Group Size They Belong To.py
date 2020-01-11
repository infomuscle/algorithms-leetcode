# 제출 코드 - Runtime 12.46 Memory 100
class Solution:
    def groupThePeople(self, groupSizes):
        answers = []
        dict = {}

        for i in range(len(groupSizes)):
            # STEP 1: dict의 키 여부 체크 후 안 찼을 경우
            if str(groupSizes[i]) in dict and len(dict[str(groupSizes[i])]) < groupSizes[i]:
                temp = dict[str(groupSizes[i])]
                temp.append(i)
                dict[str(groupSizes[i])] = temp
            # STEP 2: dict의 키 여부 체크 후 꽉 찼을 경우
            elif str(groupSizes[i]) in dict and len(dict[str(groupSizes[i])]) == groupSizes[i]:
                answers.append(dict[str(groupSizes[i])])
                temp = []
                temp.append(i)
                dict[str(groupSizes[i])] = temp
            # STEP 3: dict에 키 없으면 생성
            else:
                temp = []
                temp.append(i)
                dict[str(groupSizes[i])] = temp

        for value in dict.values():
            answers.append(value)

        return answers

# 테스트 데이터
groupSizes1 = [3,3,3,3,3,1,3]
groupSizes2 = [2,1,3,3,3,2]

# 출력
sol = Solution()
print(sol.groupThePeople(groupSizes1))
print(sol.groupThePeople(groupSizes2))

### Code 1: 성공
# def grouper(people):
#     answers = []
#     dict = {}
#
#     for i in range(len(people)):
#         isKey = True
#
#         # STEP 1: dict의 키 여부 체크 후 있으면 리스트에 ID 추가
#         if str(people[i]) in dict and len(dict[str(people[i])]) < people[i]:
#             temp = dict[str(people[i])]
#             temp.append(i)
#             dict[str(people[i])] = temp
#
#         elif str(people[i]) in dict and len(dict[str(people[i])]) == people[i]:
#             answers.append(dict[str(people[i])])
#             temp = []
#             temp.append(i)
#             dict[str(people[i])] = temp
#         # STEP 3: dict에 키 없으면 생성
#         else:
#             temp = []
#             temp.append(i)
#             dict[str(people[i])] = temp
#
#     for value in dict.values():
#         answers.append(value)
#
#     return answers