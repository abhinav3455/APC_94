def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")
print(is_palindrome(value))