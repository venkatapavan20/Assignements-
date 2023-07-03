num = int(input("Please enter a number: "))
def prime_factors(n):
    a=2
    factors=[]
    while a*a<=n:
        if n % a:
            a=a+1
        else:
            n=n//a
            factors.append(a)
    if n > 1:
        factors.append(n)
    return factors
print(prime_factors(num))