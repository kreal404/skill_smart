def ShopOLAP(N: int, items: list):
    table = {}
    for item in items:
        name, cost = item.split()
        if name in table:
            table[name] += int(cost)
        else:
            table[name] = int(cost)

    costs = sorted(set(table.values()), reverse=True)
    result = []

    for cost in costs:
        temp = {}
        for key, value in table.items():
            if value == cost:
                temp[key] = value

        for i in sorted(temp.keys()):
            result.append(f'{i} {temp[i]}')

    return result

