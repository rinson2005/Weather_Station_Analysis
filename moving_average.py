def moving_average(values, window=3):
    averages = []

    for index in range(len(values) - window + 1):
        readings = values[index:index + window]
        total = 0
        for reading in readings:
            total += reading
        average = total / window
        averages.append(float(f"{average:.1f}"))

    return averages