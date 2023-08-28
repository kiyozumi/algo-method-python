# https://algo-method.com/tasks/211

N = int(input())
A = [int(x) for x in input().split()]

max_value = max(A)
print(A.index(max_value))
