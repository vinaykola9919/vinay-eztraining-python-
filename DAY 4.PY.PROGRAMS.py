'''d={n:n*n for n in range(1,5)}
print(d)'''


'''#calculating product price for 5 units
old={"rice":60,"dal":120,"oil":150}
new={product:price*3 for(product,price) in old.items()}
print(new)'''


'''#with checks
real={"sam":24,"ram":18,"ajay":34}
now={name:age for(name,age) in real.items() if age>20}
print(now)'''



'''#dictionary


import random


cust=["sam","ram","ajay"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)'''




'''#============
import random
student_names=list(map(str,input("enter names:").split()))
marks= []
for i in range(len(student_names)):
    a=(random.randint(300,500)/500)*100
    marks.append(a)
dict={x:y for (x,y) in zip(student_names,marks)}
print(dict)'''


'''#===============


s=input("enter the string value")
ch=input("enter the character")
if ch in s:
    print("character is present:",ch)
else:
    print("character is not present")'''
'''=======================


s="madam"
if s[::-1]==s:
    print("it is a palindrome")
else:
    print("it is not a palindrome")'''

'''#==================

s=input("enter a string")
space=0
if " " in s:
    for i in s:
        if i==" ":
            space=space+1
    print(space,"sapces")
else:
            print("string doesnt contain spaces")'''
  









































 

     
