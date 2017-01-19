class MyStack(object):
    def __init__(self):
        self.stackData=[]
        self.stackMin=[]
    def push(self,value):
        self.stackData.append(value)
        if len(self.stackMin)==0:
            self.stackMin.append(value)
        if value>self.stackMin[-1]:
            self.stackMin.append(self.stackMin[-1])
        else:
            self.stackMin.append(value)

    def pop(self):
        if len(self.stackData)==0:
            raise RuntimeError("your stack is null")
        return self.stackMin.pop()

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

print(mystack.getMin())
