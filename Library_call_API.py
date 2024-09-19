from simpleAPI import Bookstore


class LibManagementSystem:
    def __init__(self, bookstore):
        self.bookstore = bookstore

    def add_book_to_store(self, id, title, author, year, genre):
        new_book = self.bookstore.add_book(id, title, author, year, genre)
        return new_book


if __name__ == "__main__":
    bookstore = Bookstore()

    adding_book = LibManagementSystem(bookstore)

    adding_book.add_book_to_store(1, "Java by Example", "Java Team", 1990, "Software")

    print(bookstore.get_book_by_id(1)["title"])