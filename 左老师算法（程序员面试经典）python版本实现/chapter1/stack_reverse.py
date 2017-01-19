def getAndRemoveLastElement(stack):
    result=stack.pop()
    if not len(stack):
        return result
    else:
        last=getAndRemoveLastElement(stack)
        stack.append(result)
        return last
def reverse(stack):
    if not len(stack):
        return
    i=getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(i)

stack=[]
stack.append(1)
stack.append(5)
stack.append(2)
stack.append(4)
# print getAndRemoveLastElement(stack)
# print getAndRemoveLastElement(stack)
reverse(stack)
print stack
