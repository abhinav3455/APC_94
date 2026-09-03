old = input("Enter word to replace: ")
new = input("Enter new word: ")

f = open("student.txt", "r")
data = f.read()
f.close()

data = data.replace(old, new)

f = open("newstudent.txt", "w")
f.write(data)
f.close()

print("File created successfully")