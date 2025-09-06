# Dictionary to store books
books = {}

# Function to add a new book
def add_book():
    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    if book_id in books:
        print(f"Book ID {book_id} already exists with name '{books[book_id]}'.")
    else:
        books[book_id] = book_name
        print(f"Book '{book_name}' added with ID {book_id}.")

# Function to remove a book
def remove_book():
    book_id = int(input("Enter Book ID to remove: "))
    if book_id in books:
        removed = books.pop(book_id)
        print(f"Book '{removed}' with ID {book_id} removed.")
    else:
        print(f"No book found with ID {book_id}.")

# Function to search for a book by ID
def search_book():
    book_id = int(input("Enter Book ID to search: "))
    if book_id in books:
        print(f"Book found: ID {book_id} → '{books[book_id]}'")
    else:
        print(f"No book found with ID {book_id}.")

# Function to display all books
def display_books():
    if books:
        print("All books in the library:")
        for book_id, book_name in books.items():
            print(f"ID {book_id} → {book_name}")
    else:
        print("No books available.")

# Menu-driven system
while True:
    print("\n=== Book Management System ===")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search a Book by ID")
    print("4. Display All Books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")