def count_vowels(string):
    count = 0
    for ch in string.lower():
        if ch in "aeiou":
            count += 1
    return count

string = input("Enter a string: ")
print(count_vowels(string))