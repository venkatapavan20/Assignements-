def lcm(x, y):
   if x > y:
       high = x
   else:
       high = y

   while(True):
       if((high % x == 0) and (high % y == 0)):
           lcm = high
           break
       high += 1

   return lcm

a = int(input("enter first number:"))
b = int(input("enter second number:"))

print(" L.C.M. :", lcm(a,b))
