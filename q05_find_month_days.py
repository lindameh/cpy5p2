def check_leap():
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

year = int(input("Enter year: "))
month = int(input("Enter month in number: "))
            

if month == 1:
    print("January {} has 31 days".format(year))
elif month == 3:
    print("March {} has 31 days".format(year))
elif month == 4:
    print("April {} has 30 days".format(year))
elif month == 5:
    print("May {} has 31 days".format(year))
elif month == 6:
    print("June {} has 30 days".format(year))
elif month == 7:
    print("July {} has 31 days".format(year))
elif month == 8:
    print("August {} has 31 days".format(year))
elif month == 9:
    print("September {} has 30 days".format(year))
elif month == 10:
    print("October {} has 31 days".format(year))
elif month == 11:
    print("November {} has 30 days".format(year))
elif month == 12:
    print("December {} has 31 days".format(year))
elif month == 2:
    if check_leap():
        print("February {} has 29 days".format(year))
    else:
        print("February {} has 28 days".format(year))
    
