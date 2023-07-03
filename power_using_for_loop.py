base=int(input("enter base:"))
exponent=int(input("enter exponent:"))
n=1

for i in range(exponent):
    n=n*base
print(n)