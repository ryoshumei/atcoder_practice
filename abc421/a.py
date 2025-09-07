def solve():
    # Step 1: input n, s[], x, y
    n = int(input())
    s = [input() for _ in range(n)]
    x, y = input().split()
    x = int(x)

    # check
    return 'Yes' if s[x - 1] == y else 'No'

# solve()
print(solve())
