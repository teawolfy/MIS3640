def leap_year(year):
    if year%4 == 0 and year%100 != 0:
        if year%400 == 0:
            print(year, " is a leap year")
    elif year%4 != 0:
        print(year, "is not a leap year")
    pass


print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))
