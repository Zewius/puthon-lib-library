from domain.DatabaseBookService import BookService


def main():
    book_service = BookService('book_database.db')
    book_service1 = BookService('book_2.db')# Указывается название файла

    # Add a book
    book_service.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 5.5, 8.5, 'Hardcover',
                          'Bookstore', '2021-01-01', None, 4, 'Great book!')

    book_service.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 5.5, 8.5, 'Hardcover',
                          'Bookstore', '2021-01-01', None, 4, 'Great book!')

    # Get all books
    all_books = book_service.get_all_books()
    for book in all_books:
        print(book)

    # Get a book by ID
    book_id = 1
    book = book_service.get_book_by_id(book_id)
    print(book)

    # Update a book
    book_service.update_book(book_id, title='The Great Gatsby', rating=5, comment='One of my favorites!')

    # Удалить книгу
    # book_service.delete_book(book_id)

    book_service.close_connection()


if __name__ == '__main__':
    main()
