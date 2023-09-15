import os

from domain.BookService import BookService


class FileBookService(BookService):
    def __init__(self, database_file):
        self.database_file = database_file

    def add_book(self, book_data):
        with open(self.database_file, 'a') as file:
            file.write(book_data + '\n')

    def get_all_books(self):
        with open(self.database_file, 'r') as file:
            return file.readlines()

    def get_books_by_title(self, title):
        with open(self.database_file, 'r') as file:
            return [line for line in file if title.lower() in line.lower()]

    def get_books_by_genre(self, genre):
        with open(self.database_file, 'r') as file:
            return [line for line in file if genre.lower() in line.lower()]

    def get_books_by_author(self, author):
        with open(self.database_file, 'r') as file:
            return [line for line in file if author.lower() in line.lower()]

    def update_book(self, book_id, new_data):
        lines = []
        with open(self.database_file, 'r') as file:
            lines = file.readlines()

        if book_id < 1 or book_id > len(lines):
            print(f"Invalid book ID: {book_id}")
            return

        lines[book_id - 1] = new_data + '\n'

        with open(self.database_file, 'w') as file:
            file.writelines(lines)

    def delete_book(self, book_id):
        lines = []
        with open(self.database_file, 'r') as file:
            lines = file.readlines()

        if book_id < 1 or book_id > len(lines):
            print(f"Invalid book ID: {book_id}")
            return

        del lines[book_id - 1]

        with open(self.database_file, 'w') as file:
            file.writelines(lines)

    def close_connection(self):
        # No connection to close in this file-based implementation
        pass


def main():
    database_file = '../book_database.txt'
    book_service = FileBookService(database_file)

    while True:
        print("1. View all books")
        print("2. Search for a book")
        print("3. Add a new book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            all_books = book_service.get_all_books()
            for book in all_books:
                print(book.strip())

        elif choice == '2':
            search_term = input("Enter the search term: ")
            search_results = book_service.get_books_by_title(search_term) + \
                             book_service.get_books_by_genre(search_term) + \
                             book_service.get_books_by_author(search_term)
            if search_results:
                for book in search_results:
                    print(book.strip())
            else:
                print("No matching books found.")

        elif choice == '3':
            title = input("Enter the book title: ")
            authors = input("Enter the author(s) (comma-separated): ")
            genre = input("Enter the genre: ")
            year = input("Enter the year of publication: ")
            width = input("Enter the width of the cover: ")
            height = input("Enter the height of the cover: ")
            binding = input("Enter the binding format (soft, hard): ")
            source = input("Enter the source of acquisition (purchase, gift, inheritance): ")
            date_added = input("Enter the date added to the library: ")
            date_read = input("Enter the date read: ")
            rating = input("Enter the rating: ")
            comment = input("Enter a comment: ")

            book_data = f"{title},{authors},{genre},{year},{width},{height},{binding},{source},{date_added},{date_read},{rating},{comment}"
            book_service.add_book(book_data)
            print("Book added successfully.")

        elif choice == '4':
            book_id = int(input("Enter the book ID to update: "))
            new_title = input("Enter the new title (leave blank to keep the existing title): ")
            new_rating = input("Enter the new rating (leave blank to keep the existing rating): ")
            new_comment = input("Enter the new comment (leave blank to keep the existing comment): ")

            book_data = book_service.get_all_books()[book_id - 1].strip().split(',')
            if new_title:
                book_data[0] = new_title
            if new_rating:
                book_data[-2] = new_rating
            if new_comment:
                book_data[-1] = new_comment

            new_data = ','.join(book_data)
            book_service.update_book(book_id, new_data)
            print("Book updated successfully.")

        elif choice == '5':
            book_id = int(input("Enter the book ID to delete: "))
            book_service.delete_book(book_id)
            print("Book deleted successfully.")

        elif choice == '6':
            book_service.close_connection()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
