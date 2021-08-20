def leap_year():
    year = int(input("Enter year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Leap year"
    else:
        return "Not a leap year"


print(leap_year())
