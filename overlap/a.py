def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        last = result[-1]
        current = intervals[i]

        if current[0] <= last[1]:  # 判断是否重叠
            # 重叠：更新last区间的终点
            last[1] = max(current[1], last[1])
        else:
            # 不重叠：直接加入新区间
            result.append(current)

    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                  # [[1,5]]
print(merge([[1,6],[2,4]]))                  # [[1,6]] ✓