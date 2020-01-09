# 제출 코드 - Runtime 48.03 Memory 57.83

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        return

    def push(self, x: int) -> None:
        self.stack1.append(x)
        return

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

obj = MyQueue()
print(obj.empty())
