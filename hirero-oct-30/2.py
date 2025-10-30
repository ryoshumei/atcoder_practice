def solution(sales, milestones):
    res = []
    m_i = 0
    temp_sales = 0
    sales_index = 0
    for i, s in enumerate(milestones):
        while temp_sales < s:
            temp_sales += sales[sales_index]
            sales_index += 1
            if sales_index >= len(sales):
                break
        if sales_index >= len(sales):
            break
        res.append(sales_index)
    if len(res) < len(milestones):
        for i in range(len(milestones) - len(res)):
            res.append(-1)
    return res

sales = [0,0,0,100,0,0]
milestones = [10,20,40,80,160]
print(solution(sales, milestones))