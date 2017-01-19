class TwoStackQueue:
    stackpush=[]
    stackpop=[]
    def add(self,n):
        self.stackpush.append(n)

    def poll(self):
        if len(self.stackpop)==0 and len(self.stackpush) ==0:
            print 'queue is empty'
        elif len(self.stackpop)==0:
            for i in range(len(self.stackpush)):
                self.stackpop.append(self.stackpush.pop())
        return self.stackpop.pop()

    def peek(self):
        if len(self.stackpop)==0 and len(self.stackpush) ==0:
            print 'queue is empty'
        elif not len(self.stackpush):
            while not len(self.stackpush):
                self.stackpop.append(self.stackpush.pop())
        return self.stackpop[-1]


queue=TwoStackQueue()
queue.add(1)
queue.add(5)
print queue.poll()
queue.add(3)
queue.add(3)
queue.add(4)
print queue.poll()
queue.add(4)
print queue.poll()
queue.add(4)
queue.add(412)
print queue.poll()
print queue.peek()
print queue.peek()
print queue.peek()
print queue.peek()
