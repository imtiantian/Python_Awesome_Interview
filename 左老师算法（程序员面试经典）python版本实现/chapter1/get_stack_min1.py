class MyStack(object):
    def __init__(self):
        self.stack=[]
        self.stackMin=[]
    def push(self,value):
        self.stack.append(value)
        if len(self.stackMin)==0:
            self.stackMin.append(value)
        if value<=self.stackMin[-1]:
            self.stackMin.append(value)
    def pop(self):
        if len(self.stack)==0:
            raise RuntimeError("your stack is empty")
        value=self.stack.pop()
        if value==self.stackMin[-1]:
            self.stackMin.pop()

    def getMin(self):
        return self.stackMin[-1]

mystack=MyStack()
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.push(1)
mystack.push(2)
mystack.push(1)
mystack.pop()
mystack.pop()
mystack.pop()

print(mystack.getMin())
