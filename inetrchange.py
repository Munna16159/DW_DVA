l=eval(input("create a list:"))
s=len(l)-1
print("list before interchanging: ",l)
temp=l[s]
l[s]=l[0]
l[0]=temp
print("list after interchanging:",l)
