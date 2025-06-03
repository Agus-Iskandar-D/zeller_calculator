# validation
def input_validation():
    while True:
        try:
            date = int(input("Plese input date (1-31): "))
            if 1 <= date <= 31:
                break
            else:
                print("Date must be within 1 and 31!")
        except ValueError:
            print("You must input number!")   
             
    while True:
        try:       
            month = int(input("Please input month (1-12): "))
            if 1 <= month <= 12:
                break
            else:
                print("Month must be within 1 and 12!")
        except ValueError:
            print("You must input number!")
    while True:
        try: 
            year = int(input("Please Input year: "))
            if year > 0:
                break
            else:
                print("Year must be positive number")
        except ValueError:
            print("You must input number!")
    return date, month, year

# leap year
def leap_year(year):
    print("\nLeap year identification:")
    for i in range(year - 2, year + 3):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(f"{i} is leap year!")
        else:
            print(f"{i} is NOT leap year!")

# Zeller’s Congruence
def day (date, month, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (date + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
    if h == 0:
        print(f"\n{date}/{month}/{year} is Saturday!")
    elif h == 1:
        print(f"\n{date}/{month}/{year} is Sunday")
    elif h == 2:
        print(f"\n{date}/{month}/{year} is Monday")
    elif h == 3:
        print(f"\n{date}/{month}/{year} is Tuesday")
    elif h == 4:
        print(f"\n{date}/{month}/{year} is Wednesday")
    elif h == 5:
        print(f"\n{date}/{month}/{year} is Thursday")
    else:
        print(f"\n{date}/{month}/{year} is Friday")

#main program
date, month, year = input_validation()
day(date, month, year)
leap_year(year)