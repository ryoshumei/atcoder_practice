def solution(arr):
    # TODO: Implement me!
    for i, num in enumerate(arr):
        arr[i] = num * 2

    return arr

arr = [1, 2, 3, 4, 5]
print(solution(arr))

