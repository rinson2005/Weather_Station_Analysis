from clean import clean


def average(values):
    if not values:
        raise ValueError("average requires at least one value")

    total = 0
    for value in values:
        total += value
    return total / len(values)


def weekly_summary(weather):
    summaries = {}
    for city in sorted(weather):
        temperatures = clean(weather[city]["temp"])
        rainfall = weather[city]["rain"]

        highest = temperatures[0]
        lowest = temperatures[0]
        for temperature in temperatures:
            if temperature > highest:
                highest = temperature
            if temperature < lowest:
                lowest = temperature

        total_rain = 0
        rainy_days = 0
        for rain_amount in rainfall:
            total_rain += rain_amount
            if rain_amount > 0:
                rainy_days += 1

        summaries[city] = (
            average(temperatures),
            highest,
            lowest,
            total_rain,
            rainy_days,
        )
    return summaries
