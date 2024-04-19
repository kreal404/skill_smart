def SumOfThe(n, data):
    total_sum = sum(data)
    for num in data:
        if num == total_sum - num:
            return num

