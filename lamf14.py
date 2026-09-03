words = input("Enter words: ").split()

result = sorted(words, key=lambda x: len(x))

print("Sorted words:", result)