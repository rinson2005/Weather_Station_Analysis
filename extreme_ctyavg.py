def extremes(averages):
    if not averages:
        print("extremes requires at least one city average")

    hottest_city = ""
    coolest_city = ""
    for city in averages:
        if hottest_city == "" or averages[city] > averages[hottest_city]:
            hottest_city = city
        if coolest_city == "" or averages[city] < averages[coolest_city]:
            coolest_city = city
    return (
        (hottest_city, averages[hottest_city]),
        (coolest_city, averages[coolest_city]),
    )
