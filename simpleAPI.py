class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, id, title, author, year, genre):
        new_book = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        }
        self.books.append(new_book)
        return new_book

    def get_book_by_id(self, id):
        for book in self.books:
            if book['id'] == id:
                return book
        return None


if __name__ == "__main__":
    bookstore = Bookstore()

    book1 = bookstore.add_book(4, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    book1 = bookstore.add_book(5, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    book1 = bookstore.add_book(6, "Python book", "Guido van Rossum", 1990, "Software")

    print(bookstore.get_book_by_id(4)["title"])
    print(bookstore.books)
