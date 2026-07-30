s = input("Enter a string: ")
no_space = ""
for ch in s:
    if not ch.isspace():
        no_space += ch
print("Without spaces:", no_space)