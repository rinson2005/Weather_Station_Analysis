def heavy_rain(weather, day_index, limit=20):
    alerts = []
    for city in sorted(weather):
        rain_amount = weather[city]["rain"][day_index]
        if rain_amount >= limit:
            alerts.append((city, rain_amount))
    return alerts


def print_rain_alerts(weather, days):
    for limit in (20, 10):
        print(f"\nRAIN ALERTS ({limit} mm or more)")
        for day_index, day in enumerate(days):
            alerts = heavy_rain(weather, day_index, limit=limit)
            if alerts:
                print(f"{day}: ", end="")
                for alert_index in range(len(alerts)):
                    city = alerts[alert_index][0]
                    rain_amount = alerts[alert_index][1]
                    if alert_index > 0:
                        print(", ", end="")
                    print(f"{city} {rain_amount} mm", end="")
                print()
