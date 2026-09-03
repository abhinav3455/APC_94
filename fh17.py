f = open("students.txt", "w")

f.write("RollNo,Name,Marks\n")
f.write("101,Amit,85\n")
f.write("102,Priya,92\n")
f.write("103,Rahul,78\n")

f.close()

f = open("students.txt", "r")
lines = f.readlines()
f.close()

print("All Records:")
for line in lines:
    print(line, end="")

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append([int(roll), name, int(marks)])

highest = max(students, key=lambda x: x[2])
average = sum(x[2] for x in students) / len(students)

print("\nHighest Marks:", highest[1], highest[2])
print("Average Marks:", average)

print("Students scoring more than 80:")
for s in students:
    if s[2] > 80:
        print(s[1], s[2])