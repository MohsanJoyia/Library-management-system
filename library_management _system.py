# Step 1: Setting up data structures
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []},
]

# Step 2: Creating the Main Menu
def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            view_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3: Implementing Book and User Functions
def view_books():
    print("\nAll Books:")
    for book in books:
        print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")


def search_books():
    search_term = input("Enter a title, author, or genre to search: ").lower()
    found_books = [book for book in books if search_term in book["title"].lower() or search_term in book["author"].lower() or search_term in book["genre"].lower()]
    
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")
    else:
        print("No books found matching your search.")

# Step 4: Borrowing and Returning Books
def borrow_book():
    user_id = int(input("Enter your User ID: "))
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        view_available_books()
        book_id = int(input("Enter the Book ID you want to borrow: "))
        book = next((b for b in books if b["id"] == book_id), None)
        if book:
            if book["status"] == "Available":
                book["status"] = "Checked Out"
                user["borrowed_books"].append(book["id"])
                print(f"You have successfully borrowed \"{book['title']}\".")
            else:
                print(f"Sorry, the book \"{book['title']}\" is currently checked out.")
        else:
            print("Invalid Book ID.")
    else:
        print("Invalid User ID.")

def return_book():
    user_id = int(input("Enter your User ID: "))
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        if user["borrowed_books"]:
            print("\nYour Borrowed Books:")
            for book_id in user["borrowed_books"]:
                book = next((b for b in books if b["id"] == book_id), None)
                print(f"{book['id']}. \"{book['title']}\"")
            
            book_id = int(input("Enter the Book ID you want to return: "))
            if book_id in user["borrowed_books"]:
                book = next((b for b in books if b["id"] == book_id), None)
                book["status"] = "Available"
                user["borrowed_books"].remove(book_id)
                print(f"You have successfully returned \"{book['title']}\".")
            else:
                print("You have not borrowed this book.")
        else:
            print("You have not borrowed any books.")
    else:
        print("Invalid User ID.")

# Step 5: User Management Functions
def view_users():
    print("\nAll Users:")
    for user in users:
        borrowed_books = [next((b["title"] for b in books if b["id"] == book_id), "Unknown") for book_id in user["borrowed_books"]]
        print(f"User {user['id']}: {user['name']}, Borrowed Books: {borrowed_books}")

#run main function
main_menu()
