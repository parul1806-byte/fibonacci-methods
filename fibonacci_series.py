#fibonacci series,0,1,1,2,3,5,8,13......
def fibonacci_series(n):
    f1,f2 = 0,1
    for i in range(n):
        print(f1,end=" ")
        f1,f2 = f2,f2+f1
fibonacci_series(9)