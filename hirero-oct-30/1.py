# sales : grid
def solution(sales):
    total = []
    for i in range(len(sales)):
        temp_total = 0
        for j in range(len(sales[i])):
            temp_total += sales[i][j]
        total.append(temp_total)
    return max(total)

sales = [[5,9],[8,1],[10,3]]
print(solution(sales))