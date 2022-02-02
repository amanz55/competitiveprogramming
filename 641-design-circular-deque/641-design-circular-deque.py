class MyCircularDeque:

    def __init__(self, k: int):
        self.myStack=[]
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.myStack.insert(0,value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.myStack.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.myStack.pop(0)
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.myStack.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.myStack[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.myStack[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.myStack)==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.myStack)==self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()