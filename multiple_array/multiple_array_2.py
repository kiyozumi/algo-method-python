# https://algo-method.com/tasks/232

N, M, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

count = 0
for i in A:
    for j in B:
        if i + j == K:
            count += 1

print(count)
