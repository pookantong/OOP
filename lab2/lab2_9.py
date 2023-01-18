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
def day_in_year(year):
    if is_leap(year):
        return 366
    return 365
def date_diff(x,y):
    first = [int(i) for i in x.split('-')]
    second = [int(i) for i in y.split('-')]
    if first[1]>12 or first[1]<1 or second[1]>12 or second[1]<1:
        return -1
    elif (first[1] == 2 and not is_leap(first[2]) and first[0] == 29) or (second[1] == 2 and not is_leap(second[2]) and second[0] == 29):
        return -1
    elif first[0]<0 or first[0]>months[first[1]-1] or second[0]<0 or second[0]>months[second[1]-1]:
        return -1
    else:
        result = day_of_year(second[0],second[1],second[2]) - day_of_year(first[0],first[1],first[2]) + 1
        for i in range(first[2],second[2]):
            result+=day_in_year(i)
        return result

print(date_diff('25-1-1999','9-11-2000'))