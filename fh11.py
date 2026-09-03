f = open("student.txt", "r")
data = f.read()
words = data.split()

longest = max(words, key=len)

print("Longest word:", longest)
f.close()