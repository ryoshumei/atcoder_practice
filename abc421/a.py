def solve():
    # Step 1: input n, s[], x, y
    n = input()
    s = []
    for i in range(int(n)):
        s.append(input())
    # print(s)
    x, y = map(str, input().split(' '))
    x = int(x)

    # check
    result = False

    if s[x - 1] == y:
        result = True
    if result is True:
        return 'Yes'
    else:
        return 'No'

# solve()
print(solve())
