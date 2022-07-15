
weather = {
    "Saterday": 20,
    "Sunday": 24,
    "Monday": 25,
    "Tuseday": 30,
    "Wdnesday": 34,
    "Thurseday": 32,
    "Friday": 33

}


new_weather = {day: temp*(9/5)+32 for (day, temp) in weather.items()}
print(new_weather)
