def sortStack(stack):
    help=[]
    while len(stack):
        cur=stack.pop()
        while len(help) and help[-1] <cur:
            print stack,help
            stack.append(help.pop())
        help.append(cur)
        print cur,stack,help
    while len(help):
        stack.append(help.pop())

stack=[4,3,2,5]
sortStack(stack)
print stack