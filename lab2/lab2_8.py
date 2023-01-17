def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def day_of_year(day, month, year):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = day
    for i in range(month-1):
        days += months[i]
    if is_leap(year) and month > 2:
        days+=1
    return days
def date_diff(x,y):
    first = [int(i) for i in x.split('-')]
    second = [int(i) for i in y.split('-')]
    result = day_of_year(second[0],second[1],second[2]) - day_of_year(first[0],first[1],first[2]) + ((second[2]-first[2])*365) + 1
    for i in range(first[2],second[2]):
        if is_leap(i):
            result+=1
    return result

print(date_diff('1-1-2018', '1-1-2020'))