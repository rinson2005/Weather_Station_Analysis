from city_average import city_average


def extremes(weather):
    averages = city_average(weather)
    if not averages:
        print("No valid city temperature averages")

    hottest_city = ""
    coolest_city = ""

    for city in averages:
        if hottest_city == "" or averages[city] > averages[hottest_city]:
            hottest_city = city

        if coolest_city == "" or averages[city] < averages[coolest_city]:
            coolest_city = city

    return (
        (hottest_city, averages[hottest_city]),
        (coolest_city, averages[coolest_city])
    )