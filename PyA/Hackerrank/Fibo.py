import time


def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


def iterative_solution(n):
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    print(second)


n = int(input())
# 33

# Recursive Benchmark
start_time = time.time()
print(fibo(n))
print(time.time() - start_time)

# Iterative Benchmark
start_time = time.time()
iterative_solution(n)
print(time.time() - start_time)
