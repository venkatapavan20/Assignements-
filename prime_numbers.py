num=int(input("enter numbers:"))
for i in range(2,num):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")

