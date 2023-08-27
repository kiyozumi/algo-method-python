# https://algo-method.com/tasks/220

N = int(input())

count = 0
for x in range(1, N + 1):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
        count += 1

print(count)
