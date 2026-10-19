def daily_rain(weather, days):
    rain_by_day = {}

    for day_index in range(len(days)):
        day = days[day_index]
        total_rain = 0
        for city in weather:
            total_rain += weather[city]["rain"][day_index]
        rain_by_day[day] = total_rain

    return rain_by_day


def rainfall_by_day(rainfall_data):
    print("RAINFALL BY DAY")
    for day in rainfall_data:
        total_rain = rainfall_data[day]
        print(f"{day:<5}{total_rain:>4} mm")

    if len(rainfall_data) > 0:
        wettest_day = ""
        wettest_total = 0

        for day in rainfall_data:
            if wettest_day == "" or rainfall_data[day] > wettest_total:
                wettest_day = day
                wettest_total = rainfall_data[day]

        print(f"Wettest day: {wettest_day} ({wettest_total} mm)")