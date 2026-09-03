books = {}

def add_book(book_id, title):
    books[book_id] = {
        "title": title,
        "available": True
    }

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return True
    return False

def return_book(book_id):
    if book_id in books and not books[book_id]["available"]:
        books[book_id]["available"] = True
        return True
    return False

def search_books(title):
    result = []

    for book_id, book in books.items():
        if title.lower() in book["title"].lower():
            result.append((book_id, book["title"]))

    return result

def display_available_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["title"])

add_book(1, "Python Programming")
add_book(2, "Data Structures")
add_book(3, "Computer Networks")

issue_book(1)

print(search_books("Python"))
display_available_books()

return_book(1)
display_available_books()