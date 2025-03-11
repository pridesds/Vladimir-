class Book:
    def init(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def str(self):
        return f'Книга "{self.name}"'

    def repr(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def init(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        return self.books[-1].id + 1 if self.books else 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if name == '123':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1


