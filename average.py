
def average(weather):
    summaries_list = []

    for city in sorted(weather):
        temperature_list = []
        temperatures = weather[city]["temp"]
        rainfall = weather[city]["rain"]

        for temperature in temperatures:
            if temperature > -50:
                temperature_list.append(temperature)

        temperature_total = 0
        for temperature in temperature_list:
            temperature_total += temperature
        avg_temp = temperature_total / len(temperature_list)

        max_temp = temperature_list[0]
        min_temp = temperature_list[0]
        for temperature in temperature_list:
            if temperature > max_temp:
                max_temp = temperature
            if temperature < min_temp:
                min_temp = temperature

        total_rain = 0
        rainy_days = 0
        for rain_amount in rainfall:
            total_rain += rain_amount
            if rain_amount > 0:
                rainy_days += 1

        summary = (city, avg_temp, max_temp, min_temp, total_rain, rainy_days)
        summaries_list.append(summary)

    return summaries_list