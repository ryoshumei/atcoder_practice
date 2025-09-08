# https://atcoder.jp/contests/abc422/tasks/abc422_a

def solve():
    # Step 1: input n, s[], x, y
    w, s = map(int, input().split('-'))
    # print(w,s)
    if s < 8:
        s += 1
    elif w < 8 and s == 8:
        s = 1
        w += 1
    return str(w) + '-' + str(s)



# solve()
print(solve())
