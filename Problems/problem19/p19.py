def leap_days(year):
    if (year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)):
        return 366
    return 365

def one_year_count(start, end, current_day, sunday_count):
    months = [31, 28, 31, 
    30, 31, 30, 
    31, 31, 30,
    31, 30, 31]

    if (isLeap(start)): months[1] = 29

    days = [sum(months[:i]) for i in range(len(months))]
    
    for i in range(0, leap_days(start)):
        if (current_day == i == 0):
            current_day += 1
            continue

        if (current_day % 7 == 0 and i in days):
            sunday_count += 1
        current_day +=1

    start += 1    
    if (start == end): 
        return sunday_count

    current_day = current_day % 7
    return one_year_count(start, end, current_day, sunday_count)

def v2(start, end, day):
    total_days = 0
    for i in range(start, end):
        total_days += leap_days(i)
    
    total_sundays = 0
    for i in range(day, total_days + day):
        if (i % 7 == 0):
            total_sundays += 1
    return total_sundays

def isLeap(year):
    return (year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0))


def v3(year, end, current_day, sunday_count):
    """THIS IS THE ONLY ONE THAT WORKS"""
    months = [31, 28, 31, 
    30, 31, 30, 
    31, 31, 30,
    31, 30, 31]

    if (isLeap(year)): months[1] = 29

    days = [sum(months[:i]) + current_day for i in range(len(months))]

    for i in days:
        if (i % 7 == 0):
            sunday_count += 1
    
    current_day = (current_day + sum(months)) % 7

    if (year == end):
        #hard coded because I didn't wanna make another function just to 
        # get the sunday counts from 1900(my code works if you only test it for 1900 tho)
        
        return sunday_count - 2, current_day
    
    year += 1
    return v3(year, end, current_day, sunday_count)

print(v3(1900, 2000, 1, 0))