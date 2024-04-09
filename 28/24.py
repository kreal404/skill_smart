def MatrixTurn(Matrix, M, N, T):
    now_layer = 1
    layers = []

    while now_layer <= min(M, N) / 2:
        temp_layer = []
        for i in range(now_layer - 1, M - now_layer + 1):
            if i < now_layer - 1 or i > M - now_layer:
                continue

            if i in [now_layer - 1, M - now_layer]:
                if i < M // 2:
                    if now_layer == 1:
                        start = None
                        stop = None
                        reverse = 1
                    else:
                        start = now_layer - 1
                        stop = -now_layer + 1
                        reverse = 1
                else:
                    if now_layer == 1:
                        start = None
                        stop = None
                        reverse = -1
                    else:
                        start = -now_layer
                        stop = now_layer - 2
                        reverse = -1

                for num in map(int, list(Matrix[i][start:stop:reverse])):
                    temp_layer.append(num)
            else:
                temp_layer.append(int(Matrix[i][-now_layer]))

        for i in range(M - now_layer - 1, now_layer - 1, -1):
            if i < now_layer - 1 or i > M - now_layer:
                continue

            temp_layer.append(int(Matrix[i][now_layer - 1]))

        layers.append(temp_layer)
        now_layer += 1

    for i in range(len(layers)):
        temp_layer = layers[i]
        temp_layer = temp_layer[-T:] + temp_layer[:-T]
        layers[i] = temp_layer

    new_matrix = [['' for _ in range(N)] for _ in range(M)]
    now_layer = 1

    for layer in layers:
        layer_index = 0
        for i in range(now_layer - 1, M - now_layer + 1):
            if i < now_layer - 1 or i > M - now_layer:
                continue

            if i in [now_layer - 1, M - now_layer]:
                if i < M // 2:
                    if now_layer == 1:
                        start = 0
                        stop = N
                        reverse = 1
                    else:
                        start = now_layer - 1
                        stop = N - now_layer + 1
                        reverse = 1
                else:
                    if now_layer == 1:
                        start = N - 1
                        stop = -1
                        reverse = -1
                    else:
                        start = N - now_layer
                        stop = now_layer - 2
                        reverse = -1

                for j in range(start, stop, reverse):
                    new_matrix[i][j] = str(layer[layer_index])
                    layer_index += 1
            else:
                new_matrix[i][-now_layer] = str(layer[layer_index])
                layer_index += 1

        for i in range(M - now_layer - 1, now_layer - 1, -1):
            if i < now_layer - 1 or i > M - now_layer:
                continue

            new_matrix[i][now_layer - 1] = str(layer[layer_index])
            layer_index += 1

        now_layer += 1

    for i in range(M):
        Matrix[i] = ''.join(new_matrix[i])

