s = input("Enter a string: ")

vowels = set("aeiouAEIOU")
v = c = d = sp = sc = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    elif ch.isspace():
        sp += 1
    else:
        sc += 1
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)
print("Special characters:", sc)