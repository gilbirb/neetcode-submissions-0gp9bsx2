class MinStack:

    def __init__(self):
        self.stack = []
        self.minPrefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 1:
            self.minPrefix.append(min(val, self.minPrefix[-1]))
        else:
            self.minPrefix.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minPrefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minPrefix[len(self.stack) - 1]