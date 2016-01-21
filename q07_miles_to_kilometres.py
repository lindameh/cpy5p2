print("Miles Kilometers Kilometers Miles")
for i in range(1,11):
    km1 = i * 1.609
    km2 = (i + 3) * 5
    miles = km2 / 1.609
    print("{0:<5}".format(i), "{0:<10.3f}".format(km1), "{0:<10}".format(km2), "{0:.3f}".format(miles))
