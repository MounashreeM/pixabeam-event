'''def function(name,end):
    print("hello",name)
    print(end)
    return "done"
a=function("mouna","thank")    
b=function("harry","hi")
print(a)
print(b)'''
"""def fact(n):
    if n==0 or n==1:
      return 1
    else:
     return n*fact(n-1)

n=int(input("enter no"))
print(fact(n))"""
"""def greatest(a,b,c):
    if((a>b and a>c)):
        print(f"a is greatest,{a}")
    elif(b>c and b>a):
        print(f"b is greatest,{b}")    
    else:
        print("c is greater",c)    
a,b,c=2,4,5  
greatest(a,b,c)"""


"""print("a")
print("b")
print("c",end=" ")
print("d")"""
"""def sum(n):
    if n==1:
        return 
    else:
        return sum(n-1)+n
n=int(input("enter no"))    
print(sum(n))"""

'''def multi(n):
    if n == 0:
        return ""
    else:
        print("*" * n)
        multi(n - 1)

multi(5)'''
def rem(l,word):
    for item in l:
     l.remove(word)
     return l
l=["harr","prem","rahl"]
print(rem(l,"rahl"))

