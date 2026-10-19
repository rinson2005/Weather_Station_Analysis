from average import average
from clean import clean


def city_averages(weather):
    averages = {}
    for city in sorted(weather):
        temperatures = clean(weather[city]["temp"])
        if len(temperatures) > 0:
            averages[city] = average(temperatures)
    return averages
