class Book:
    pages_of_material = "материал: бумага"
    text_presence = True

    def __init__(self, book_title, author, number_of_pages, ISBN, flag_reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.flag_reserved = flag_reserved


class SchoolBook(Book):
    def __init__(self, book_title, author, number_of_pages, ISBN, flag_reserved, lesson, group, assignments=True ):
        super().__init__(book_title, author, number_of_pages, ISBN, flag_reserved)
        self.lesson = lesson
        self.group = group
        self.assignments = assignments


def book_list(book):
    reserved = ", зарезервирована" if book.flag_reserved else ""
    print(f"Название: {book.book_title}, Автор: {book.author},"
          f" страниц: {book.number_of_pages}, {book.pages_of_material}{reserved}")

def school_book_list(school_books):
    reserved = ", зарезервирована" if school_books.flag_reserved else ""
    print(f"Название: {school_books.book_title}, Автор: {school_books.author}, страниц: {school_books.number_of_pages},"
          f" предмет {school_books.lesson}, класс: {school_books.group}{reserved}")


copy_1 = Book("Идиот", "Достоевский", 500, True, True)
copy_2 = Book("Малахитовая шкатулка", "Бажов", 315, True, False)
copy_3 = Book("Сердце пармы", "Иванов", 315, True, True)
copy_4 = Book("Пиковая дама", "Пушкин", 315, True, True)
copy_5 = Book("Тестирование Дот Ком", "Савин", 315, True, True)
textbook = SchoolBook(
    "Алгебра",
    "Иванов",
    200,
    None,
    True,
    "Математика",
    9
)
textbook_1 = SchoolBook(
    "Логика",
    "Виноградов",
    318,
    None,
    False,
    "Логика подраздел",
    8
)


book_list(copy_1)
book_list(copy_2)
school_book_list(textbook)
school_book_list(textbook_1)
