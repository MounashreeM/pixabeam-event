
# n =int(input("enter no"))
# i=0
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)
"""n =int(input("enter no"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)   """ 
'''n =int(input("enter no"))
for i in range(n+1):
    
    print("*" * (2*i-1),end="" )
    print((" " * (n-i)),end="")
    print("")
    '''
'''def good(name="mint"):
    gr= "good day"+" "+name
    return gr 
a=good("mouna")
b=good()   
print(b)
print(a)'''
def fact(n):
    if n==0 :
        return 0
    else:
        return n+fact(n-1)
    
a=fact(5) 
print(a) 