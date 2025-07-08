# fibonacci series nth term with recursion
def fibonacci(n):
    if n <= 1:
        return(n)
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fab = fibonacci(7)
print(fab)