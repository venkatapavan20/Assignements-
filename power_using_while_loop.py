base=int(input("enter base:"))
exponent=int(input("enter exponent:"))
n=1

while exponent>0:
    n=n*base
    exponent=exponent-1
print(n)