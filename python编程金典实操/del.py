class Employee:
    count=0
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
        Employee.count+=1
        print "constructor is %s,%s"%(self.firstname,self.lastname)
    def __del__(self):
        Employee.count-=1
        print "destructor is %s,%s"%(self.lastname,self.firstname)
print Employee.count
employee1 = Employee('a','b')
employee2 = Employee('c','d')
employee3 = employee1
print Employee.count
del employee1
del employee2
del employee3
print Employee.count
