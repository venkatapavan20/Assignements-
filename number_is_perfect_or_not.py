a = int(input(" Give the number : "))
m=0
for i in range(1,(a//2)+1):
    remainder = (a % i)
    if remainder == 0:
        m = m + i
if m == a:
    print("Given number is perfect ")
else:
    print("Given number is not a perfect") 
