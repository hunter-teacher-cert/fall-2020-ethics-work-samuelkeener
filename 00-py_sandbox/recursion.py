# Sam Keener
# Aug 2020

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("Good News Everyone!")
print(f"5! = {factorial(5)}" )
print(f"fib(8) = {fib(8)}" )

