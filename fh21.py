def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    f = open("books.txt", "a")
    f.write(book_id + "," + title + "," + author + ",Available\n")
    f.close()

def search_book():
    book_id = input("Enter book ID: ")
    f = open("books.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if data[0] == book_id:
            print(data)

    f.close()

def issue_book():
    book_id = input("Enter book ID: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")
        if data[0] == book_id and data[3] == "Available":
            data[3] = "Issued"
        f.write(",".join(data) + "\n")

    f.close()

def return_book():
    book_id = input("Enter book ID: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")
        if data[0] == book_id:
            data[3] = "Available"
        f.write(",".join(data) + "\n")

    f.close()

def available_books():
    f = open("books.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if data[3] == "Available":
            print(data)

    f.close()

add_book()
search_book()
issue_book()
return_book()
available_books()