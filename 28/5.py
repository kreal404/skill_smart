def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)

    id_to_salary = {}

    for i in range(N):
        id_to_salary[sorted_ids[i]] = sorted_salary[i]

    result = []

    for id in ids:
        result.append(id_to_salary[id])

    return result


