months = [31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def day_of_year(day, month, year):
    days = day
    for i in range(month-1):
        days += months[i]
    if is_leap(year) and month > 2:
        days+=1
    return days