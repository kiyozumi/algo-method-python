# https://algo-method.com/tasks/233

X, Y, Z = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

count = 0
for i in A:
    for j in B:
        for k in C:
            if i + j == k:
                count += 1

print(count)
