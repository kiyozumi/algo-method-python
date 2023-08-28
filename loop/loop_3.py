# https://algo-method.com/tasks/238

L, R = [int(x) for x in input().split()]


def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(length):
        if s[i] != s[length - 1 - i]:
            return False

    return True


result = 0
for n in range(L, R + 1):
    s = str(n)
    if is_palindrome(s):
        result += 1

print(result)
