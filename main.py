import os
import time
import math

def collatz(n, cache):
    steps = 0
    while n != 1:
        if n in cache:
            return steps + cache[n]
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n = 3 * n + 1
            steps += 1 + math.log2(n)
    return steps

def solve_collatz_conjecture(limit):
    cache = {1: 0}
    max_steps = 0
    num = 0
    start_time = time.perf_counter()
    elapsed_time = 0
    sample_interval = 1000
    smoothing_factor = 0.1
    estimated_time = 0
    for i in range(2, limit+1):
        steps = collatz(i, cache)
        cache[i] = steps
        if steps > max_steps:
            max_steps = steps
            num = i
        elapsed_time = time.perf_counter() - start_time
        estimated_time = (1 - smoothing_factor) * estimated_time + smoothing_factor * elapsed_time * (limit / i)
        if i % sample_interval == 0:
            print(f"Elapsed time: {elapsed_time:.2f}s. Estimated time remaining: {estimated_time - elapsed_time:.2f}s.", end="\r")
    print()
    return num

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("The number that produces the longest Collatz sequence under 1000000 is: ", solve_collatz_conjecture(1000000))
