'''n=int(input("enter the no"))
if (i<1):
    for i in range(2,n):
        if(n%i==0):
          print("prime not")
          break
        else:
         print(f"prime is {n}")    
    else:
     print("not prime")  '''
'''list=["sf","ggh","soi"]
for item in list:
    if(item.startswith("s")):
        print(item)'''
# n=int(input("enter no"))
# for i in range(1,11):
#     print(f"{n}*{11-i}={n*(11-i)}")
# n1=int(input("enter no"))
# n2=int(input("enter no"))
# n3=int(input("enter no"))
# n4=int(input("enter no"))
# averg=(n1+n2+n3+n4)/400
# if(averg>=40):
#     print(" ou are pass",averg)
# else:
#     print("no")    
"""post=input("enter the message")
mess=input("enter")
if mess.lower() in post.lower():
   print("yes ")
else:
   print("no")   """

""""l=["hhh","kkk","fgh"]
for name in l:
    if(name.startswith)('k'):
        print(f"heloo {name}")"""""
"""n=int(input("enter no"))
for i in range(11):
    print(f"{n}*{i}={n*i}")"""
'''n =int(input("enter no"))
for i in range(2,n):
    if(n%i)==0:
        print("not prine")
        break
else:
        print("prime")    '''
    
st=" hi this is mouna"

f=open("C:/Users/Admin/Desktop/chapter1/file.py","w")
f.write(st)

f.close()
with open("C:/Users/Admin/Desktop/chapter1/file.py") as f:
    print(f.read())