import sqlite3

from domain.BookService import BookService


class DatabaseBookService(BookService):
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """ Создание новой таблицы """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                authors TEXT,
                genre TEXT,
                year INTEGER,
                cover_width REAL,
                cover_height REAL,
                binding_format TEXT,
                source TEXT,
                date_added TEXT,
                date_read TEXT,
                rating INTEGER,
                comment TEXT
            )
        ''')
        self.conn.commit()

    def add_book(self, title, authors, genre, year, cover_width, cover_height, binding_format, source, date_added,
                 date_read, rating, comment):
        """ Добавление новой информации о книге """
        self.cursor.execute('''
            INSERT INTO books (title, authors, genre, year, cover_width, cover_height, binding_format, source, date_added, date_read, rating, comment)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            title, authors, genre, year, cover_width, cover_height, binding_format, source, date_added, date_read,
            rating,
            comment))
        self.conn.commit()

    def get_all_books(self):
        """ Получить список всех книг """
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()

    def get_book_by_id(self, book_id):
        """ Получить книгу по индивидуальному идентификатору из таблицы """
        self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        return self.cursor.fetchone()

    def update_book(self, book_id, title=None, authors=None, genre=None, year=None, cover_width=None, cover_height=None,
                    binding_format=None, source=None, date_added=None, date_read=None, rating=None, comment=None):
        """ Обновить информацию о книге """
        update_query = 'UPDATE books SET '
        update_values = []

        if title:
            update_query += 'title = ?, '
            update_values.append(title)
        if authors:
            update_query += 'authors = ?, '
            update_values.append(authors)
        if genre:
            update_query += 'genre = ?, '
            update_values.append(genre)
        if year:
            update_query += 'year = ?, '
            update_values.append(year)
        if cover_width:
            update_query += 'cover_width = ?, '
            update_values.append(cover_width)
        if cover_height:
            update_query += 'cover_height = ?, '
            update_values.append(cover_height)
        if binding_format:
            update_query += 'binding_format = ?, '
            update_values.append(binding_format)
        if source:
            update_query += 'source = ?, '
            update_values.append(source)
        if date_added:
            update_query += 'date_added = ?, '
            update_values.append(date_added)
        if date_read:
            update_query += 'date_read = ?, '
            update_values.append(date_read)
        if rating:
            update_query += 'rating = ?, '
            update_values.append(rating)
        if comment:
            update_query += 'comment = ?, '
            update_values.append(comment)

        update_query = update_query.rstrip(', ') + ' WHERE id = ?'
        update_values.append(book_id)

        self.cursor.execute(update_query, tuple(update_values))
        self.conn.commit()

    def delete_book(self, book_id):
        """ Удалить информацию о книге """
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.conn.commit()

    def close_connection(self):
        """ Завершить работу с базой данных """
        self.cursor.close()
        self.conn.close()
