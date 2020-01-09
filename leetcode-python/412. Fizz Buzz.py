# 제출 코드 - Runtime 77.54 Memory 39.26
class Solution:
    def fizzBuzz(self, n: int):

        answer = []
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                answer.append(str(i))
                continue
            tmp = ""
            if i % 3 == 0:
                tmp += "Fizz"
            if i % 5 == 0:
                tmp += "Buzz"
            answer.append(tmp)

        return answer


n1 = 15

sol = Solution()
print(sol.fizzBuzz(n1))
