n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
def gcd(n1, n2):
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller+1):
        if(n1 % i == 0 and n2 % i == 0):
            gcd = i
    return gcd
print("GCD: ", gcd(n1, n2))
