# https://algo-method.com/tasks/221

N = int(input())

count = 0
for x in range(1, N + 1):
    if N % x == 0:
        count += 1

print(count)
