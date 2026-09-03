f = open("attendance.txt", "w")
f.write("101,Amit,70,100\n")
f.write("102,Priya,85,100\n")
f.write("103,Rahul,60,100\n")
f.close()

f = open("attendance.txt", "r")

for line in f:
    roll, name, present, total = line.strip().split(",")
    percentage = int(present) / int(total) * 100
    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

f.close()