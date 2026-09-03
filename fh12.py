f = open("student.txt", "r")
data = f.read()
words = data.split()

d = {}

for word in words:
    word = word.lower()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)
f.close()