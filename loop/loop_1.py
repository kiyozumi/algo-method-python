# https://algo-method.com/tasks/234

N = int(input())
A = [int(x) for x in input().split()]


def is_prime(n: int) -> bool:
    if n == 1:
        return False

    is_prime = True
    for x in range(2, n):
        if n % x == 0:
            is_prime = False

    return is_prime


count = 0
for x in A:
    if is_prime(x):
        count += 1

print(count)
