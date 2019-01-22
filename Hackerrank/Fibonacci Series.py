import time


def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def iterative_solution(n):
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    print(second)


n = int(input())
# Would recommend a maximum input of 33

# Recursive Benchmark
start_time = time.time()
print(recursive_fibonacci(n))
print(time.time() - start_time)

# Iterative Benchmark
start_time = time.time()
iterative_solution(n)
print(time.time() - start_time)
