def solve():
    def reverse_int(n):
        reversed_str = str(abs(n))[::-1]
        return int(reversed_str)

    # Step 1: get x, y
    x, y = map(int, input().split())
    # print(x, y)

    a = [0, x, y]
    a.append(reverse_int(a[1] + a[2]))

    for i in range(4, 11):
        # print(i, reverse_int(a[i - 1] + a[i - 2]))
        # if i == 4:
        #     print('i : ', i, i - 1, i - 2, a[i - 1], a[i - 2], a[i - 1] + a[i - 2])
        #     print(reverse_int(a[i - 1] + a[i - 2]))
        # if i == 5:
        #     print('i : ', i, i - 1, i - 2, a[i - 1], a[i - 2], a[i - 1] + a[i - 2])
        #     print('a[4]', a[4])
        #     print(reverse_int(a[i - 1] + a[i - 2]))
        a.append(reverse_int(a[i - 1] + a[i - 2]))
        # if i == 4:
        #     print(reverse_int(a[i - 1] + a[i - 2]))
        #     print('a[i - 1] + a[i - 2])',a[i - 1] + a[i - 2])
        #     print('a[i]', a[i])
        #     print('a[]', a)

    print(a[10])

    # check

solve()
# print(solve())
