# Caching
from functools import cache, lru_cache
import time

# calculate time
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
print(fibonacci(35))
end = time.time()
print(end - start)

# vs cache
@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
print(fibonacci(35))
end = time.time()
print(end - start)


# lru_cache - caches the last resently used cache maxsize represents
# the ammount of cache value kept, oldest one del to make room for the new one
# @lru_cache(maxsize=10)
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(100))


# @cache - caches all the results
# @cache
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(100))


# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(8))