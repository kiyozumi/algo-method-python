# https://algo-method.com/tasks/237


def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(length):
        if s[i] != s[length - 1 - i]:
            return False

    return True


N = int(input())
strings = [input() for _ in range(N)]

count = 0
for s in strings:
    if is_palindrome(s):
        count += 1

print(count)
