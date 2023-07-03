

def GCD_or_HCD(a, b):

	if a > b:
		small = b
	else:
		small = a
	for i in range(1, small + 1):
		if((a % i == 0) and (b % i == 0)):
			gcd = i
			
	return gcd

a =int(input("enter num:"))
b = int(input("enter num:"))

# prints 12
print ("The gcd and hcd: ", end="")
print (GCD_or_HCD(a,b))
