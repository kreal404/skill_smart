def odometer(oksana: list) -> int:
    distance = 0
    prev_time: 0
    
    for i in range(len(oksana)):
        if i % 2 == 0:
            speed = oksana[i]
            time = oksana[i + 1]
            distance += speed * (time - prev_time)
            prev_time = time

    return distance

