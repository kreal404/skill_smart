def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def Football(F, N):
    if is_sorted(F):
        return True

    for i in range(N):
        for j in range(i+1, N):
            F[i], F[j] = F[j], F[i]
            if is_sorted(F):
                return True
            F[i], F[j] = F[j], F[i]

    for i in range(N):
        for j in range(i+1, N):
            if F[i] > F[j]:
                start = i
                while start < N-1 and F[start] > F[start+1]:
                    start += 1
                F[i:start+1] = reversed(F[i:start+1])
                if is_sorted(F):
                    return True
                F[i:start+1] = reversed(F[i:start+1])

    return False

