class PhoneNumber:
    def __init__(self,number):
        self.areaCode = number[1:4]
        self.exchange = number[6:9]
        self.line = number[10:14]
    def __str__(self):
        return "(%s)%s-%s"%(self.areaCode,self.exchange,self.line)
def test():
    nn = raw_input('nn:')
    phone = PhoneNumber(nn)
    print phone
if __name__ =="__main__":
    test()