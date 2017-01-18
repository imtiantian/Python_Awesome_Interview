class Node:
    def __init__(self):
        self.data=None
        self.nextNode=None
    def set_and_return_Next(self):
        self.nextNode=Node()
        return self.nextNode
    def getNext(self):
        return self.nextNode
    def getData(self):
        return self.data
    def setDate(self,d):
        self.data=d