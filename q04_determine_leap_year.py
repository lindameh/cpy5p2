year = int(input("Enter year: "))
if year % 4 ==0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap")
    else:
        print("Non-leap")
else:
    print("Non-leap")
