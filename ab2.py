
ch = input("Enter a character: ")


if len(ch) == 1 and ch.isalpha():
    if ch.lower() in "aeiou":
        print(ch, "is a vowel.")
    else:
        print(ch, "is a consonant.")
else:
    print("Please enter a single alphabet.")
