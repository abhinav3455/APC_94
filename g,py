import math

num = int(input("Enter a number: "))

if num < 0:
    print("Invalid input")
else:
    root = int(math.isqrt(num))
    if root * root != num:
        print("Square root is not an integer")
    else:
        if root < 2:
            print("Square root is not prime")
        else:
            is_prime = True
            for i in range(2, int(root ** 0.5) + 1):
                if root % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"Square root ({root}) is prime")
            else:
                print(f"Square root ({root}) is not prime")