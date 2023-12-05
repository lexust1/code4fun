# Lines
N = 3
# Columns
M = 4
# Wrong
A = [[0] * M] * N
print(A[0] == A[1])
print(A[0] is A[1])

# Correct
B = [[0] * M for _ in range(N)]
print(B[0] == B[1])
print(B[0] is B[1])
