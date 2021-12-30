#Display everything in seconds. In its current iteration this is wrong!
def main():
    week_input = int(input("Please enter the number of weeks: "))
    day_input = int(input("Please enter the number of days: "))
    hour_input = int(input("Please enter the number of hours: "))
    minute_input = int(input("Please enter the number of minutes: "))
    a = f1(minute_input)
    b = f2(hour_input)
    c = f3(day_input)
    d = f4(week_input)
    print("The total number of seconds is ",a + b + c +d)
#Need to convert minutes to seconds
def f1(minutes):
    seconds = minutes * 60
    return seconds
#convert hours to minutes
def f2(hours):
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
#convert days to hours
def f3(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
#Convert weeks to days
def f4(weeks):
    days = weeks * 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
if __name__ == "__main__":
    main()
