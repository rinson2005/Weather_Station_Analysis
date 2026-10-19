from average import weekly_summary
from city_average import city_averages
from clean import clean_weather
from daily_rain import daily_rain, print_rainfall_summary
from day_type import print_city_day_types
from extreme_ctyavg import extremes
from heavy_rain import print_rain_alerts
from moving_average import print_moving_average


days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
weather = {
    "Kochi": {
        "temp": [31, 32, 30, 29, 31, 33, 32],
        "rain": [0, 5, 12, 20, 0, 0, 3],
    },
    "Munnar": {
        "temp": [18, 19, 17, 16, 18, 20, 19],
        "rain": [2, 8, 15, 25, 5, 0, 4],
    },
    "Palakkad": {
        "temp": [36, 37, 38, -999, 37, 39, 38],
        "rain": [0, 0, 0, 0, 0, 0, 0],
    },
    "Kozhikode": {
        "temp": [30, 31, 30, 29, 30, 32, 31],
        "rain": [0, 10, 8, 18, 2, 0, 1],
    },
}


print("SENSOR CHECK")
print("-" * 30)
cleaned_temperatures, invalid_counts = clean_weather(weather)
for city in sorted(weather):
    print(f"{city:<10} {invalid_counts[city]} invalid reading(s)")

print("\nWEEKLY SUMMARY")
print(
    f"{'City':<10} {'Avg':>7} {'Max':>6} {'Min':>6}"
    f" {'Rain':>7} {'Rainy':>7}"
)
weekly_summaries = weekly_summary(weather)
for city in sorted(weather):
    summary = weekly_summaries[city]
    avg_temp, highest, lowest, total_rain, rainy_days = summary
    print(
        f"{city:<10} {avg_temp:>7.1f} {highest:>6}"
        f" {lowest:>6} {total_rain:>7} {rainy_days:>7}"
    )

print("\nDAY TYPES")
print(f"{'City':<10}{'Hot':>5}{'Warm':>6}{'Cool':>6}")
print_city_day_types(weather, cleaned_temperatures)

hottest, coolest = extremes(city_averages(weather))
print(f"\nHottest city: {hottest[0]} ({hottest[1]:.1f})")
print(f"Coolest city: {coolest[0]} ({coolest[1]:.1f})")

rainfall_by_day = daily_rain(weather, days)
print("\nRAINFALL BY DAY")
print_rainfall_summary(rainfall_by_day, days)

print_rain_alerts(weather, days)

print("\nKOCHI 3-DAY MOVING AVERAGE")
print_moving_average(weather["Kochi"]["temp"], days)
