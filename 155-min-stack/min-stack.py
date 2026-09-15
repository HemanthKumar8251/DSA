class MinStack:

    def __init__(self):
        self.st = []

    def push(self, value: int) -> None:
        min_val = self.getMin()
        if min_val != None and min_val<value:
            self.st.append([value,min_val])
        else:
            self.st.append([value,value])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()