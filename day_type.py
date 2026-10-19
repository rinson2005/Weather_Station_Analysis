def day_type(temp, hot=35, warm=28):
    if temp >= hot:
        return "Hot"
    elif temp >= warm:
        return "Warm"
    else:
        return "Cool"


def count_day_types(temperatures):
    counts = {}
    for temperature in temperatures:
        label = day_type(temperature)
        if label in counts:
            counts[label] = counts[label] + 1
        else:
            counts[label] = 1
    return counts


def print_city_day_types(weather, cleaned_temperatures):
    for city in sorted(weather):
        counts = count_day_types(cleaned_temperatures[city])
        print(
            f"{city:<10}{counts.get('Hot', 0):>5}"
            f"{counts.get('Warm', 0):>6}{counts.get('Cool', 0):>6}"
        )
