def add_time(initial_time, added_time, day=None):
    # setting constants
    week_list = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    midday = None

    # initial_time Get hours
    seperator = initial_time.find(":")
    if initial_time[-2:] == "PM":
        midday = True
    hour = int(initial_time[0:seperator])
    if midday:
        hour = hour + 12

    # initial_time get minutes
    minutes = int(initial_time[seperator + 1 : seperator + 3])
    initial_minutes = minutes + (hour * 60)

    # added_time Get hours
    seperator = added_time.find(":")
    hour = int(added_time[0:seperator])

    # initial_time get minutes
    minutes = int(added_time[seperator + 1 : seperator + 3])
    added_minutes = minutes + (hour * 60)

    # Final time
    final_minutes = initial_minutes + added_minutes
    hours = int(final_minutes / 60)
    final_minutes = str(final_minutes % 60)
    final_hours = hours % 24
    days = str(int(hours / 24))
    if final_hours - 12 >= 0:
        period = "PM"
        final_hours = final_hours - 12
        if final_hours == 0:
            final_hours = 12
    else:
        period = "AM"
        final_hours = final_hours

    if final_hours == 0:
        final_hours = 12

    final_hours = str(final_hours)

    # String formatting.
    suffix = ""
    if day != None:
        if days != "0":
            weekday = days
            while True:
                try:
                    day = week_list[week_list.index(day.lower()) + int(weekday)]
                    break
                except:
                    print("Excepted", weekday)
                    weekday = int(weekday) - 7
        days = str(days)
        suffix = ", " + day.title()
    if days == "1":
        suffix = suffix + " (next day)"
    elif days != "0":
        suffix = suffix + " (" + days + " days later)"

    return "{0}:{1} {2}{3}".format(final_hours, final_minutes.zfill(2), period, suffix)


print(add_time("11:43 PM", "24:20", "tueSday"))
print("12:03 AM, Thursday (2 days later)")
print("\n---")
print(add_time("8:16 PM", "466:02", "tuesday"))
print("6:18 AM, Monday (20 days later)")
print("\n")
