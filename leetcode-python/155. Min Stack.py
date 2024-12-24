# 제출 코드 - Runtime 89.91 Memory 6.34
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2 ** 31
        return

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))
        return

    def pop(self) -> None:
        popped = self.stack.pop()
        self.min = self.stack[-1][1] if self.stack else 2 ** 31
        return

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
