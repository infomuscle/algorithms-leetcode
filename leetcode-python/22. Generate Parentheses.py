# 제출 코드 - Runtime 54.63 Memory 39.34
class Solution:

    def generateParenthesis(self, n: int):
        remain_open = ["("] * (n - 1)
        remain_close = [")"] * n
        stack = []
        current = "("
        p = []
        self.__addParenthesis(stack, current, remain_open, remain_close, p)

        return p

    def __addParenthesis(self, stack, current, remain_open, remain_close, p):
        if len(remain_open) == 0 and len(remain_close) == 0:
            if len(stack) == 0:
                p.append(current)
            return

        if len(remain_open) > 0:
            t_stack = stack[:]
            t_remain_open = remain_open[:]
            t_current = current[:]
            t_open = t_remain_open.pop()
            t_stack.append(t_open)
            t_current += t_open
            self.__addParenthesis(t_stack, t_current, t_remain_open, remain_close[:], p)

        if len(remain_close) > 0:
            t_stack = stack[:]
            t_remain_close = remain_close[:]
            t_current = current[:]
            t_close = t_remain_close.pop()
            if len(t_stack) > 0 and t_stack[-1] == "(":
                t_stack.pop()
            t_current += t_close
            self.__addParenthesis(t_stack, t_current, remain_open[:], t_remain_close, p)

        return


sol = Solution()

n1 = 3
n2 = 1
print(sol.generateParenthesis(n1))
print(sol.generateParenthesis(n2))
