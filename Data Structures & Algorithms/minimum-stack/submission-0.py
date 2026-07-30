class MinStack:
    # 1 => core [1] minStack [1]
    # 2 => core [1,2] minStack [1,min(1,2)] => [1,1]
    # 0 => core [1,2,0] minStack [1,1,min(1,0)] => [1,1,0]
    # getMin => 0
    # pop => core [1,2], minStack [1,1]
    # top => 2
    # getMin => 1

    def __init__(self):
        self.core = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        self.core.append(val)

    def pop(self) -> None:
        self.core.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.core[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
