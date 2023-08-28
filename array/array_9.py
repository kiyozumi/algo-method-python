# https://algo-method.com/tasks/217

N = int(input())
A = [int(x) for x in input().split()]
result = [0] * 9

for x in A:
    result[x - 1] += 1

for x in result:
    print(x)
