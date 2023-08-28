# https://algo-method.com/tasks/260

N = int(input())
S = [input() for _ in range(N)]

import collections

c = collections.Counter(S)
if N != len(c):
    print("Yes")
else:
    print("No")
