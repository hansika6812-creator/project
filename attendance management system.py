students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Present (P) / Absent (A): ")
    students[name] = status

print("\nAttendance Record")
for name in students:
    print(name, ":", students[name])