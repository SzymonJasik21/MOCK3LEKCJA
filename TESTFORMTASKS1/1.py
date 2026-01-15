class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open == True:
            if self.current_page < self.pages:
                self.current_page += 1
            return True
        else:
            return "Book is closed"

    def status(self):
        return f"{self.title}, {self.author}, pages: {self.pages}, current: {self.current_page}, open: {self.is_open}"

if __name__ == "__main__":
    book = EBook("Python Basics", "John Doe", 100)
    book.open()
    book.next_page()
    print(book.status())
    book.close()
    print(book.next_page())