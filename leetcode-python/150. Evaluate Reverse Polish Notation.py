# 제출 코드 - Runtime 19.93 Memory 13.40

# Intuition
# 스택을 사용하면 될 것 같은데.
# 숫자 -> push, 기호 -> pop 2번 & 연산 & push
# 곱하기 나누기 더하기 빼기 순서 보장이 되나?
# 예시만 보면 되는데 medium인 이유가 있을 것 같기도..
# 일단 해보자

# Approach
# stack 만들고
# token for tokens
# if 숫자 -> push
# else -> pop, pop, calculate, push
# 모든 인풋이 올바른 연산이라는 보장이 있나? -> 있다
import math


class Solution:
    def evalRPN(self, tokens):

        stack = []
        for token in tokens:
            if self.is_integer(token):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()  # 1개만 있을 수 있나 ->
                result = self.calculate(token, num1, num2)
                stack.append(result)

        return stack.pop()

    def is_integer(self, num_str):
        try:
            int(num_str)
            return True
        except:
            return False

    def calculate(self, token, num1, num2):
        if token == "+":
            return num1 + num2
        if token == "-":
            return num1 - num2
        if token == "*":
            return num1 * num2
        if token == "/":
            # + -
            temp = num1 / num2
            if temp >= 0:
                return math.floor(temp)
            else:
                return math.ceil(temp)  # 안 나눠떨어지는 경우는.. 역시.. 분수를 표현? -> truncates toward zero
