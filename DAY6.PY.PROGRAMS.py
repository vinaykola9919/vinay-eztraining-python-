'''a=100
b=0

try:#u r telling this may hv error,u try
    print(a/b)

#except Exception:#u saying if error the i handle
#print("cant divide any number by zero")


except Exception as e:
    print("please note,number cant be divide by zero")
finally:print("bye")   '''

#=========================================================

'''a=10
b=0

try:
    print("resource open")
    print(a/b)


except Exception as e:
    print("dont give second no.as zero",e)
    print("resource closed")               '''
#=========================================================
'''
x=10
if x%2!=0:
    raise Exceptiion("x shud b even number")
else:
    print("x is even number..correct")     '''
#=========================================================
'''
class computer:
    def conflig(self):
        print("YEs")

lenova=computer()
lenova.conflig

dell=computer()
dell.conflig()   '''
#========================================================
'''
class Employee:
    def __init__(self,name,id):
     self.id=id
     self.name=name

    def display(self):
        print(self.id,self.name)

emp1=Employee("John",101)
emp2=Employee("David",102)


emp1.display()
emp2.display()'''
#========================================================
'''class  computer():
    a=10
    b=20
    print("class  variable inside class",a)


    def conflig(self):
        c=100
        print("YEs")
        print("Instance access",self.b)

lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.conflig()'''

#======================================================== 

























