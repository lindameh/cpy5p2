n = int(input("Enter the number of students: "))
arr = [[0 for i in range(n)] for i in range(2)]
i = 0
for i in range(n):
    arr[0][i] = input("Enter the student's name:  ")
    arr[1][i] = float(input("Enter the student's score: "))
    
index = arr[1].index(max(arr[1]))
print("Student with the highest score:", arr[0][index], arr[1][index])
arr[0].remove(arr[0][index])
arr[1].remove(arr[1][index])

index = arr[1].index(max(arr[1]))
print("Student with the second highest score:", arr[0][index], arr[1][index])

