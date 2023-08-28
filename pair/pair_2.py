# https://algo-method.com/tasks/245

L, R = [int(x) for x in input().split()]

count = 0
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        if i % 10 == j % 10:
            count += 1

print(count)
