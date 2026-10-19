def heavy_rain(weather, day_index, limit=20):
    alerts = []
    for city in sorted(weather):
        rainfall = weather[city]["rain"][day_index]
        if rainfall >= limit:
            alert = (city, rainfall)
            alerts.append(alert)
    return alerts


def rain_alerts(weather, days):
    limits = [20, 10]
    for limit in limits:
        print(f"\nRAIN ALERTS ({limit} mm or more)")
        for day_index in range(len(days)):
            day = days[day_index]
            alerts = heavy_rain(weather, day_index, limit=limit)
            if len(alerts) > 0:
                print(f"{day}: ", end="")
                for alert_index in range(len(alerts)):
                    city = alerts[alert_index][0]
                    rainfall = alerts[alert_index][1]
                    if alert_index > 0:
                        print(", ", end="")
                    print(f"{city} {rainfall} mm", end="")
                print()
