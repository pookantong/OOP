months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def day_of_year(day, month, year):
    days = day
    for i in range(month):
        days += months[i]
    if is_leap(year) and month > 2:
        days+=1
    return days
def day_in_year(year):
    if is_leap(year):
        return 366
    return 365
def date_diff(x,y):
    first = [int(i) for i in x.split('-')]
    second = [int(i) for i in y.split('-')]
    result = day_of_year(second[0],second[1],second[2]) - day_of_year(first[0],first[1],first[2]) + 1
    for i in range(first[2],second[2]):
        result+=day_in_year(i)
    return result

print(date_diff('1-1-2018', '1-12-2020'))