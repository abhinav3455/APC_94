s = input("Enter a sentence: ")

result = ""
new_word = True
for ch in s:
    if ch.isspace():
        result += ch
        new_word = True
    elif new_word and ch.isalpha():
        result += ch.upper()
        new_word = False
    else:
        result += ch.lower()
        new_word = False

print("Title case:", result)