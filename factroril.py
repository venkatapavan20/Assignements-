def factorail(f):
    if f==0:
        return 1
    else:
        return(f*factorail(f-1))

num=int(input("enter number:"))
print(factorail(num))