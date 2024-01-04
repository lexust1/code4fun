# Comparison between Recursive and Dynamic Programming Approaches for Factorial

# Recursive Approach (factorial_recursive):
#   Pros:
#     - Simplicity: The code is straightforward and easy to understand.
#     - Conciseness: Requires fewer lines of code.
#   Cons:
#     - Efficiency: Less efficient for large 'n' due to multiple
#     function calls overhead.
#     - Stack Overflow Risk: Deep recursion may lead to stack overflow
#     for large values of 'n'.
#     - Recursion Depth Limit: Python's maximum recursion depth limits
#     the maximum value of 'n'.

# Dynamic Programming Approach (factorial_dynamic_programming):
#   Pros:
#     - Efficiency: More efficient for large 'n', avoids repeated
#     function calls overhead.
#     - No Stack Overflow Risk: Iterative method eliminates stack
#     overflow risks.
#     - Scalability: Can handle much larger values of 'n' without
#     hitting recursion depth limits.
#   Cons:
#     - Memory Usage: Requires additional memory to store intermediate
#     factorial values.
#     - Complexity: Slightly more complex and less intuitive than the
#     recursive version.

# Conclusion:
# For small values of 'n', both methods are effective, and the choice
# may hinge on readability (favoring recursion).
# However, for large values of 'n', the dynamic programming approach
# is more effective and robust, avoiding the limitations and
# inefficiencies of deep recursion.
import time
import sys


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_dp(n):
    fact_values = [1] * (n + 1)
    for i in range(2, n + 1):
        fact_values[i] = i * fact_values[i-1]
    return fact_values[n]


def main():
    # 1000
    print(f"The Python recursion limit: {sys.getrecursionlimit()}")
    sys.setrecursionlimit(10000)
    print(f"The Python recursion limit: {sys.getrecursionlimit()}")
    start_time = time.time()
    rec = factorial_recursive(9000)
    end_time = time.time()
    print(f"The recursive time:{end_time - start_time}")
    start_time = time.time()
    dp = factorial_dp(9000)
    end_time = time.time()
    print(f"The dynamic programming time:{end_time - start_time}")


if __name__ == "__main__":
    main()
