num=int(input("enter numbers:"))

sum=0

for i in range(num):
    numbers=float(input("enter input numbers:"))
    sum=sum+numbers
avg = sum/num
print("average:", avg)