fib_memo = {0:0, 0:0}   #fib memoization

def fib(n):
    if(not(n in fib_memo)):
        fib_memo[n] = fib(n-1) + fib(n-2)

    return fib_memo[n]
