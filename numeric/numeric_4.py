# https://algo-method.com/tasks/224

A, B = [int(x) for x in input().split()]

ans = 0
for x in range(1, min(A, B) + 1):
    if A % x == 0 and B % x == 0:
        ans = x

print(ans)
