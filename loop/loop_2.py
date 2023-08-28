# https://algo-method.com/tasks/235

N, K = [int(x) for x in input().split()]

result = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if K == count:
        result += 1

print(result)
