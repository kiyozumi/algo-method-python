# https://algo-method.com/tasks/231

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

count = 0
for i in A:
    for j in B:
        if i > j:
            count += 1

print(count)
