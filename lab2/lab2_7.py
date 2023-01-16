def day_of_year(day, month, year):
    is_leap(year)

def is_leap(year):
    if year % 4 == 0:
        return "leap_year"
    else :
        return "Not leap_year"