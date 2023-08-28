# https://algo-method.com/tasks/244

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

count = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] <= K:
            count += 1

print(count)
