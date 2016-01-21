def verify_input():
    if 0 <= score <= 100:
        return True
    else:
        return False
    
score = float(input("Enter score: "))

if verify_input():
    if score >= 70:
        print("A")
    elif score >= 60:
        print("B")
    elif score >= 55:
        print("C")
    elif score >= 50:
        print("D")
    elif score >= 45:
        print("E")
    elif score >= 35:
        print("S")
    else:
        print("U")
else:
    print("Invalid! Score must be within 0 - 100.")
