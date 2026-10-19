def day_type(weather, hot=35, warm=28):
    summaries_list = []
    for city in sorted(weather):
        hot_days = 0
        warm_days = 0
        cool_days = 0

        if "temp" in weather[city]:
            for temperature in weather[city]["temp"]:
                if temperature is not None and temperature >= -50:
                    if temperature >= hot:
                        hot_days += 1
                    elif temperature >= warm:
                        warm_days += 1
                    else:
                        cool_days += 1

        summary = (city, hot_days, warm_days, cool_days)
        summaries_list.append(summary)
    return summaries_list