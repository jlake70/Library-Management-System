class Book:
    def __init__(self, title, author, status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Status: {self.status}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"

class Author:
    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id

    def __str__(self):
        return f"Author ID: {self.author_id}, Name: {self.name}"



class BookOperations:
    def __init__(self):
        self.books = {}

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        if title in self.books:
            print(f"Book '{title}' already exists.")
        else:
            book = Book(title, author)
            self.books[title] = book
            print(f"Book '{title}' added successfully.")
        

    def borrow_book(self):
       
        title = input("Enter the title of the book to borrow: ")
        if title in self.books:
            book = self.books[title]
            if book.status == "Available":
                book.status = "Borrowed"
                print(f"You have borrowed '{title}'.")
            else:
                print(f"'{title}' is already borrowed.")
        else:
            print(f"Book '{title}' not found.")
        

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        if title in self.books:
            book = self.books[title]
            if book.status == "Borrowed":
                book.status = "Available"
                print(f"'{title}' has been returned.")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"Book '{title}' not found.")
        

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        if title in self.books:
            print(self.books[title])
        else:
            print(f"Book '{title}' not found.")

        

    def display_books(self):
        if self.books:
            for title, book in self.books.items():
                print(book)
        else:
            print("No books available.")
        

class UserOperations:
    def __init__(self):
        self.users = {}

    def add_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        if user_id in self.users:
            print(f"User ID '{user_id}' already exists.")
        else:
            user = User(name, user_id)
            self.users[user_id] = user
            print(f"User '{name}' added successfully.")

    def view_user(self):
        user_id = input("Enter the user ID to view: ")
        if user_id in self.users:
            print(self.users[user_id])
        else:
            print(f"User ID '{user_id}' not found.")

    def display_users(self):
        if self.users:
            for user_id, user in self.users.items():
                print(user)
        else:
            print("No users available.")

class AuthorOperations:
    def __init__(self):
        self.authors = {}

    def add_author(self):
        author_id = input("Enter author ID: ")
        name = input("Enter author name: ")
        if author_id in self.authors:
            print(f"Author ID '{author_id}' already exists.")
        else:
            author = Author(name, author_id)
            self.authors[author_id] = author
            print(f"Author '{name}' added successfully.")

    def view_author(self):
        author_id = input("Enter the author ID to view: ")
        if author_id in self.authors:
            print(self.authors[author_id])
        else:
            print(f"Author ID '{author_id}' not found.")

    def display_authors(self):
        if self.authors:
            for author_id, author in self.authors.items():
                print(author)
        else:
            print("No authors available.")
