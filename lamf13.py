words = input("Enter words: ").split()

result = list(filter(lambda x: len(x) > 5, words))

print("Words:", result)