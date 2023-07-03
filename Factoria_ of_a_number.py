num=int(input("enter the number:"))
a=1
if num<0:
    print("no factorial")
elif num==0:
    print("this is 1")
else:
    for i in range(1,num+1):
        a=a*i
    print(a)