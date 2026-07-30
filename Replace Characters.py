s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")
replaced = ""
for ch in s:
    if ch == old:
        replaced += new
    else:
        replaced += ch
print("After replacement:", replaced)