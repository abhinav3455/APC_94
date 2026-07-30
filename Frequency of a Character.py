s = input("Enter a string: ")
ch = input("Character to count: ")
cnt = 0
for x in s:
    if x == ch:
        cnt += 1
print(f"Frequency of '{ch}':", cnt)