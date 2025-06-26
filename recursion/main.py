'''
n = int(input("Enter a number: "))

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 3
        a, b = 0, 1
        while i <= n:
            c = a + b
            a, b = b, c
            i += 1 
        return c

print(f"The Fibonacci term for the {n}th place is: ", fibo(n))
'''
"""
#using the recursion 
def fibo(n):
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the term position: "))
print(f"The {n}th Fibonacci term is:", fibo(n))
"""

#optimization 
