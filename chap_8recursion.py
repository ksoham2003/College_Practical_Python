def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_rec(n-1)

f = factorial_rec(0)
print(f)

#factorial program without using recurion 
#num = int(input("enter the number\n"))
#factorial = 1
#for i in range(1,num+1):
 #   factorial = factorial * i
#print(f"the factorial of number is {factorial}")
     