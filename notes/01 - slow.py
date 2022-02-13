def fib(n):
    '''Takes in a number n, and returns the nth fibonacci number, starting with: 1, 1, 2, 3, 5,...'''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
