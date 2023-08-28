# https://algo-method.com/tasks/259

N = int(input())
A = [int(x) for x in input().split()]

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[j] == max(A[i], A[j], A[k]):
                count += 1
print(count)
