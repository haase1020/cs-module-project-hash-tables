# 0,1,1,2,3,5,8,13,21,34
# recursive
# base case
# call itself
# move in the direction of the base case
# finds the n-th number in the fibonacci sequence

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


# print(fib(30))
# print(fib(5))
# print(fib(6))

# using caching and recursion - memoization or top-down dynamic programming
cache = {}


def fib(n):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    else:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]


print(fib(50))
