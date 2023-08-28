# https://algo-method.com/tasks/222
N = int(input())

if N == 1:
    print("No")
    exit()

for x in range(2, N):
    if N % x == 0:
        print("No")
        exit()

print("Yes")
