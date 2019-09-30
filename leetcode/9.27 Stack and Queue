class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__ordered=[]
        self.__stack=[]

    def push(self, x: int) -> None:
        self.__stack.append(x)
        self.__ordered.append(min([x]+self.__ordered[-1:]))

    def pop(self) -> None:
        for i in [self.__stack,self.__ordered]:
            i.pop() 


    def top(self) -> int:
        return self.__stack[-1]


    def getMin(self) -> int:
        return self.__ordered[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
