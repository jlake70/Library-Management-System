from library_system import BookOperations, UserOperations, AuthorOperations

class LibraryManagementSystem:
    def __init__(self):
        self.book_operations = BookOperations()
        self.user_operations = UserOperations()
        self.author_operations = AuthorOperations()

    def main_menu(self):
        while True:
            try:
                print("\nWelcome to the Library Management System!")
                print("Main Menu:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Add a new user")
                print("7. View user details")
                print("8. Display all users")
                print("9. Add a new author")
                print("10. View author details")
                print("11. Display all authors")
                print("12. Quit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.book_operations.add_book()
                elif choice == '2':
                    self.book_operations.borrow_book()
                elif choice == '3':
                    self.book_operations.return_book()
                elif choice == '4':
                    self.book_operations.search_book()
                elif choice == '5':
                    self.book_operations.display_books()
                elif choice == '6':
                    self.user_operations.add_user()
                elif choice == '7':
                    self.user_operations.view_user()
                elif choice == '8':
                    self.user_operations.display_users()
                elif choice == '9':
                    self.author_operations.add_author()
                elif choice == '10':
                    self.author_operations.view_author()
                elif choice == '11':
                    self.author_operations.display_authors()
                elif choice == '12':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 12.")

            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
                
LibraryManagementSystem().main_menu()