# https://algo-method.com/tasks/227

S = input()

last_idx = len(S) - 1
for i, c in enumerate(S):
    if c != S[last_idx - i]:
        print("No")
        exit()

print("Yes")
