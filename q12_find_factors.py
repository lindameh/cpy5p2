integer = int(input("Enter a positive integer: "))
arr = []
i = 2
while integer != 1:
    while integer % i == 0:
        arr.append(str(i))
        integer /= i
    i += 1
print(", ".join(arr))
              
