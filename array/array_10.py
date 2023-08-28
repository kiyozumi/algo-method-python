# https://algo-method.com/tasks/219

N = int(input())
A = [int(x) for x in input().split()]
result = [0] * 9

for x in A:
    result[x - 1] += 1

max_count = max(result)
print(result.index(max_count) + 1)

# another way
# import collections
# c = collections.Counter(A)
# print(max(c))
