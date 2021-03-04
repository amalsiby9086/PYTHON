n_terms = int(input("Number of terms: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Enter a positive integer")
elif n_terms == 1:
    print("Fibonacci series:",n1)
elif n_terms == 1:
    print("Fibonacci series:",n1,n2)
else:
    print("Fibonacci series:")
    while count < n_terms:
        print(n1,end = " ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
