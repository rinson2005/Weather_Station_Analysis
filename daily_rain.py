def daily_rain(weather, days):
    rainfall = {}
    for day_index, day in enumerate(days):
        total_rain = 0
        for city in weather:
            total_rain += weather[city]["rain"][day_index]
        rainfall[day] = total_rain
    return rainfall


def print_rainfall_summary(rainfall, days):
    for day in days:
        print(f"{day:<5}{rainfall[day]:>4} mm")

    wettest_day = ""
    for day in days:
        if wettest_day == "" or rainfall[day] > rainfall[wettest_day]:
            wettest_day = day
    print(f"Wettest day: {wettest_day} ({rainfall[wettest_day]} mm)")
