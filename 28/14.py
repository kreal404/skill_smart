def Unmanned(L, N, track):
    time = 0
    last_pos = 0

    for traffic_light_info in track:
        pos, red, green = traffic_light_info

        if pos > L:
            break

        time += pos - last_pos

        traffic_light = time % (red + green)

        if traffic_light < red:
            time += red - traffic_light

        last_pos = pos

    time += L - last_pos

    return time

