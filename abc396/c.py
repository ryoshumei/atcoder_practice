def solve():
    # Step 1: 输入和排序
    n, m = map(int, input().split())
    black = list(map(int, input().split()))
    white = list(map(int, input().split()))

    # 对black和white进行什么排序？
    black.sort(reverse=True)
    white.sort(reverse=True)
    # Step 2: 计算所有正值黑球的总和
    # 计算positive_black_sum和positive_black_count
    positive_black_sum = 0
    positive_black_count = 0
    for b in black:
        if b > 0:
            positive_black_sum += b
            positive_black_count += 1

    # Step 3: 枚举白球数量
    max_value = 0

    white_sum_list = []
    white_sum_list.append(0)
    black_sum_list = []
    black_sum_list.append(0)

    for w in range(1,m + 1):
        white_sum_list.append(white_sum_list[w - 1] + white[w - 1])
    for n in range(1,n + 1):
        black_sum_list.append(black_sum_list[n - 1] + black[n - 1])

    # w means how many white balls we select
    for w in range(min(m, n) + 1):
        # 更新white_sum（加上第w个白球的价值）
        white_sum = white_sum_list[w]
        # 计算这种情况下的总价值
        if positive_black_count < w:
            value = white_sum + black_sum_list[w]
        else:
            value = positive_black_sum + white_sum

        # 提示：需要考虑positive_black_count和w的关系
        # 更新max_value
        if value > max_value:
            max_value = value
    return max_value
print(solve())
