num1 = int(input("Given number:"))
num2 = int(input("Given number:"))
def add(a, b):
    while b != 0:
        c = a & b
        a = a ^ b
        b = c << 1
    return a

sum = add(num1, num2)
print(sum)