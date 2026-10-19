def city_average(weather):
    averages = {}

    for city in weather:
        valid_temperatures = []
        if "temp" in weather[city]:
            for temperature in weather[city]["temp"]:
                if temperature is not None and temperature > -50:
                    valid_temperatures.append(temperature)

        if len(valid_temperatures) > 0:
            temperature_total = 0
            for temperature in valid_temperatures:
                temperature_total += temperature
            averages[city] = temperature_total / len(valid_temperatures)

    return averages