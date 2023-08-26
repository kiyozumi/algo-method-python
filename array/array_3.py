# https://algo-method.com/tasks/212

N = int(input())
A = [int(x) for x in input().split()]

count = 0
for x in A:
    if x > 0:
        count += 1

print(count)
