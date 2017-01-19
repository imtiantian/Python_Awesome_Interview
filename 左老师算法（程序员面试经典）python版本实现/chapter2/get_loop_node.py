class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

def GetLoopNode(head):
    if head==None or head.next==None or head.next.next==None:
        return None
    n1=head.next
    n2=head.next.next
    while n1!=n2:
        if n2.next==None or n2.next.next==None:
            return None
        n2=n2.next.next
        n1=n1.next
    n2=head
    while n1!=n2:
        n1=n1.next
        n2=n2.next
    return n1

#1->2->3->4->5->6->7->4...
head1 = Node(1)
head1.next =Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next = head1.next.next.next

print GetLoopNode(head1).value


