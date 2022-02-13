def fib(n):
    '''Takes in a number n, and returns the nth fibonacci number, starting with: 1, 1, 2, 3, 5,...'''
    if n<=1:
        return n
    else:
        f = [0, 1]
        for i in range(2,n+1):
            f.append(f[i-1] + f[i-2])
        return f[n]
