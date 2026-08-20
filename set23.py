available_books = {"Python", "Java", "C++", "DBMS", "Operating System"}
requested_books = {"Python", "DBMS", "Networking"}

available = available_books & requested_books

print("Requested books available:", available)