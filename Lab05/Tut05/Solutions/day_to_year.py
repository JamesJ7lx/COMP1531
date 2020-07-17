from is_leap_year import is_leap_year

# Changed this to upper case to satisfy pylint
ORIGIN_YEAR = 1970

# One of many possible ways to write this function.
def day_to_year(days):
    year = ORIGIN_YEAR

    while days > 0:
        if is_leap_year(year):
            days -= 366
        else:
            days -= 365
        year += 1

    return year - 1
