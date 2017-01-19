class Node(object):
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class PreInPosTraversal(object):
    def preOrderRecur(self,head):
        if head is None:
            return
        print head.value,
        self.preOrderRecur(head.left)
        self.preOrderRecur(head.right)

    def inOrderRecur(self,head):
        if head is None:
            return
        self.inOrderRecur(head.left)
        print head.value,
        self.inOrderRecur(head.right)

    def posOrderRecur(self,head):
        if head==None:
            return
        self.posOrderRecur(head.left)
        self.posOrderRecur(head.right)
        print head.value,

if __name__=="__main__":
    test=PreInPosTraversal()
    head=Node(5)
    head.left=Node(3)
    head.right=Node(8)
    head.left.left=Node(2)
    head.left.right=Node(4)
    head.left.left.left=Node(1)
    head.right.left=Node(7)
    head.right.left.left=Node(6)
    head.right.right=Node(10)
    head.right.right.left=Node(9)
    head.right.right.right=Node(11)

    print"=========recursive=========="
    print "pre-order: "
    test.preOrderRecur(head)
    print "in-order: ",
    test.inOrderRecur(head)
    print "pos-order: ",
    test.posOrderRecur(head)



