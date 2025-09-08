def solve():
    def check_cell(i, j):
        black_count = 0
        new_i, new_j = get_up(i, j)
        if is_in_range(new_i, new_j) and s[new_i][new_j] == '#':
            black_count += 1

        new_i, new_j = get_down(i, j)
        if is_in_range(new_i, new_j) and s[new_i][new_j] == '#':
            black_count += 1

        new_i, new_j = get_left(i, j)
        if is_in_range(new_i, new_j) and s[new_i][new_j] == '#':
            black_count += 1

        new_i, new_j = get_right(i, j)
        if is_in_range(new_i, new_j) and s[new_i][new_j] == '#':
            black_count += 1

        return black_count == 2 or black_count == 4

    def get_up(i, j):
        return i - 1, j
    def get_down(i, j):
        return i + 1, j
    def get_left(i, j):
        return i, j - 1
    def get_right(i, j):
        return i, j + 1
    def is_in_range(i, j):
        return 0 <= i < h and 0 <= j < w

    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if check_cell(i, j) == False:
                    print('No')
                    return
    print('Yes')


    # check

solve()
# print(solve())
