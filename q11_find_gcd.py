n1 = int(input("Enter a positive integer: "))
n2 = int(input("Enter another postive integer: "))
a = [n1, n2]
a.sort()
d = a[0]
while a[0] % d != 0 or a[1] % d != 0:
    d -= 1
print("The greatest common divisor is", d)
