def clean(weather):
    invalid_counts = {}
    for city in sorted(weather):
        temp_readings = 0
        if "temp" in weather[city]:
            for temperature in weather[city]["temp"]:
                if temperature is None or temperature < -50:
                    temp_readings += 1
        invalid_counts[city] = temp_readings
        print(f"{city:<10} {temp_readings} invalid reading(s)")
    return invalid_counts