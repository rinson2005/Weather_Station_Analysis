def clean(values):
    cleaned_values = []
    for value in values:
        if value is not None:
            if value >= -50:
                cleaned_values.append(value)
    return cleaned_values


def clean_weather(weather):
    cleaned_temperatures = {}
    invalid_counts = {}
    for city in sorted(weather):
        raw_temperatures = weather[city]["temp"]
        cleaned_temperatures[city] = clean(raw_temperatures)
        invalid_count = len(raw_temperatures) - len(cleaned_temperatures[city])
        invalid_counts[city] = invalid_count
    return cleaned_temperatures, invalid_counts
