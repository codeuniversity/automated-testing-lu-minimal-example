def fib(n):
    '''Takes in a number n, and returns the nth fibonacci number, starting with: 1, 1, 2, 3, 5,...'''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
# let's test this...
print(fib(5)) # is this correct?
print(fib(20)) # is this correct?
# seems to work!
# but no automatic feedback :(
# => have to check manually
assert(fib(5) == 5)
assert(fib(20) == 6765)
# cool, still works, and it verifies automatically!
# what happens if it's wrong?
assert(fib(5) == 7)
# cool, it gives me an error!
# this is an automated test!
# (why is this useful?)
# let's try out fib(50)
# # someone give me that number please
assert(fib(50) == 12586269025)
# let's start...
# ...
# ...
# ...
# ...well, that seems very slow
# let's rewrite the implementation!
def fib(n):
    '''Takes in a number n, and returns the nth fibonacci number, starting with: 1, 1, 2, 3, 5,...'''
    if n<=1:
        return n
    else:
        f = [0, 1]
        for i in range(2,n+1):
            f.append(f[i-1] + f[i-2])
        return f[n]
# ...tests still pass, so it seems to work! :D
