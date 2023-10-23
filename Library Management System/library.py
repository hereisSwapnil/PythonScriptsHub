class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book_title, author, pages, year, publisher, genre, language, copies):
        if book_title == "" or author == "" or pages == "" or year == "" or publisher == "" or genre == "" or language == "" or copies <= 0:
            print("Please fill out all the fields.")
        elif book_title not in self.books:
            book = {
                "title": book_title,
                "author": author,
                "pages": pages,
                "year": year,
                "publisher": publisher,
                "genre": genre,
                "language": language,
                "copies": copies
            }
            self.books.append(book)
            print(f'Book "{book_title}" by {author} added successfully.')
        else:
            print(f'Book "{book_title}" already exists in the library.')

    def display_books(self):
        if self.books == []:
            print("No books in the library.")
        else:
            print("Available Books:")
            for book in self.books:
                print(f'"{book["title"]}" by {book["author"]}')

    def book_info(self, book_title):
        book = None
        for b in self.books:
            if book_title == b["title"]:
                book = b
        if book:
            print(f'"{book["title"]}" by {book["author"]}')
            print(f'Pages: {book["pages"]}')
            print(f'Year: {book["year"]}')
            print(f'Publisher: {book["publisher"]}')
            print(f'Genre: {book["genre"]}')
            print(f'Language: {book["language"]}')
            print(f'Copies: {book["copies"]}')
        else:
            print(f'Book "{book_title}" does not exist in the library.')

    def borrow_book(self, book_title, student):
        if student.books == {} or book_title not in [book["title"] for book in student.books]:
            book = None
            for b in self.books:
                if book_title == b["title"]:
                    book = b
            if book:
                book["copies"] -= 1
                if book_title not in self.borrowed_books:
                    self.borrowed_books[book_title] = [student.name]
                else:
                    self.borrowed_books[book_title].append(student.name)
                student.borrow_book(book_title, b["title"])
                print(f'You have borrowed "{book_title}". Enjoy reading!')
            else:
                print(f'Sorry, "{book_title}" is not available in the library.')
        else:
            print(f'You have already borrowed "{book_title}".')
            


    def return_book(self, book_title, student):
        if book_title not in [book["title"] for book in student.books]:
            print(f'You have not borrowed "{book_title}".')
        else:
            book = None
            for b in self.books:
                if book_title == b["title"]:
                    book = b
            if book:
                book["copies"] += 1
                self.borrowed_books[book_title].remove(student.name)
                student.return_book(book_title)
                print(f'Thank you for returning "{book_title}".')

    def borrowed_books_func(self):
        if self.borrowed_books == {}:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book_title in self.borrowed_books:
                print(f'->"{book_title}" Borrowed by')
                for student in self.borrowed_books[book_title]:
                    print(f'    {student}')

class Student:
    def __init__(self, name):
        self.name = name
        self.books = []
        print(f"Welcome to the library, {self.name}!")

    def borrow_book(self, book_title, author):
        book = {
            "title": book_title,
            "author": author
        }
        self.books.append(book)

    def return_book(self, book_title):
        for book in self.books:
            if book_title == book["title"]:
                self.books.remove(book)

    def borrowed_books(self):
        if self.books == []:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book in self.books:
                print(f'"{book["title"]}" by {book["author"]}')

def main():
    library = Library()
    student = Student(input("Enter your name: "))

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book (Librarian Only)")
        print("2. Display Available Books")
        print("3. Display Book's Information")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. See Student's Borrowed Books")
        print("7. See Total Borrowed Books (Librarian Only)")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ").lower()
            author = input("Enter author name: ")
            pages = int(input("Enter number of pages: "))
            year = int(input("Enter year published: "))
            publisher = input("Enter publisher: ")
            genre = input("Enter genre: ")
            language = input("Enter language: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, pages, year, publisher, genre, language, copies)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter book title: ").lower()
            library.book_info(title)
        elif choice == "4":
            title = input("Enter the title of the book you want to borrow: ").lower()
            library.borrow_book(title, student)
        elif choice == "5":
            title = input("Enter the title of the book you are returning: ").lower()
            library.return_book(title, student)
        elif choice == "6":
            student.borrowed_books()
        elif choice == "7":
            library.borrowed_books_func()
        elif choice == "8":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()