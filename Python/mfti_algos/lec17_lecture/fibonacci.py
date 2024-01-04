# Comparison between Recursive and Dynamic Programming Approaches for
# Fibonacci Sequence

# Recursive Approach (fibonacci_recursive):
#   Pros:
#     - Simplicity: Straightforward and easy to understand implementation.
#     - Direct Approach: Closely follows the mathematical definition
#     of the Fibonacci sequence.
#   Cons:
#     - Inefficiency: High for large 'n' due to redundant computations
#     of the same values.
#     - Stack Overflow Risk: Deep recursion can lead to stack overflow
#     for large values of 'n'.
#     - Recursion Depth Limit: The approach is limited by Python's
#     maximum recursion depth.

# Dynamic Programming Approach (fibonacci_dynamic_programming):
#   Pros:
#     - Efficiency: Significantly more efficient for large 'n', as
#     it avoids redundant calculations.
#     - Scalability: Can compute large Fibonacci numbers without the
#     risk of stack overflow.
#   Cons:
#     - Memory Usage: Requires additional memory to store the Fibonacci
#     numbers up to 'n'.
#     - Slightly More Complex: More complex than the recursive
#     approach, though still straightforward.

# Conclusion:
# For small values of 'n', the recursive method is sufficient and easy
# to understand.
# However, for larger values, the dynamic programming approach is much
# more efficient and practical,
# avoiding the computational inefficiency and stack overflow risks
# associated with deep recursion.
import time
import sys


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dp(n):
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values[n]


def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_dp_no_append(n):
    fib_values = [0] * (n + 1)
    fib_values[1] = 1
    for i in range(2, n + 1):
        fib_values[i] = fib_values[i-1] + fib_values[i-2]
    return fib_values[n]


def main():
    # # 1000
    # print(f"The Python recursion limit: {sys.getrecursionlimit()}")
    # sys.setrecursionlimit(10000)
    # print(f"The Python recursion limit: {sys.getrecursionlimit()}")
    n = 37
    start_time = time.time()
    rec = fibonacci_recursive(n)
    end_time = time.time()
    print(f"The recursive time:{end_time - start_time}")
    start_time = time.time()
    dp = fibonacci_dp(n)
    end_time = time.time()
    print(f"The dynamic programming time:{end_time - start_time}")
    start_time = time.time()
    rec_memo = fibonacci_dp(n)
    end_time = time.time()
    print(f"The recursive time with memoization:{end_time - start_time}")
    start_time = time.time()
    rec_memo = fibonacci_dp_no_append(n)
    end_time = time.time()
    print(f"The recursive time with memoization:{end_time - start_time}")


if __name__ == "__main__":
    main()

