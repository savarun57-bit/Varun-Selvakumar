print("=== Student Grade Calculator ===")

name = input("Enter Student Name: ")

tamil = int(input("Tamil Mark: "))
english = int(input("English Mark: "))
maths = int(input("Maths Mark: "))
science = int(input("Science Mark: "))
social = int(input("Social Mark: "))

total = tamil + english + maths + science + social
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
