side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))

a = [side_1, side_2, side_3]
a.sort()
if a[0] + a[1] > a[2]:
    perimeter = side_1 + side_2 + side_3
    print("Perimeter =", perimeter)
else:
    print("Invalid triangle!")
