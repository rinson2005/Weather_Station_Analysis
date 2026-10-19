from average import average


def moving_average(values, window=3):
    if window <= 0:
        raise ValueError("window must be greater than zero")

    averages = []
    for index in range(len(values) - window + 1):
        readings = values[index:index + window]
        averages.append(float(f"{average(readings):.1f}"))
    return averages


def print_moving_average(values, days, window=3):
    averages = moving_average(values, window)
    for index, value in enumerate(averages):
        ending_day = days[index + window - 1]
        print(f"{ending_day:<5}{value:>5.1f}")
