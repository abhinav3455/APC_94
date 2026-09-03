word = input("Enter word to search: ")

f = open("student.txt", "r")
count = 0
lines = []

for i, line in enumerate(f, 1):
    n = line.lower().split().count(word.lower())
    if n > 0:
        count += n
        lines.append(i)

print("Occurrences:", count)
print("Line numbers:", lines)

f.close()