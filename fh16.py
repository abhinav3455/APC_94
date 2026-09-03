f = open("student.txt", "r")
data = f.read()
f.close()

g = open("uppercase.txt", "w")
g.write(data.upper())
g.close()

print("Uppercase file created")