# https://algo-method.com/tasks/216

N, V = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

idx = -1
for i, x in enumerate(A):
    if V == x:
        idx = i

print(idx)
