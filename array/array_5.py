# https://algo-method.com/tasks/215

N = int(input())
A = [int(x) for x in input().split()]

count = 0
for idx in range(N - 1):
    if A[idx] < A[idx + 1]:
        count += 1
print(count)
