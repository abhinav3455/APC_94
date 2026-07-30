s = input("Enter a sentence: ")
words = s.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)