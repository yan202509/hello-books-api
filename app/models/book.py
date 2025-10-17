class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "1984", "A dystopian novel by George Orwell."),
    Book(2, "To Kill a Mockingbird", "A novel by Harper Lee about racial injustice."),
    Book(3, "The Great Gatsby", "A novel by F. Scott Fitzgerald about the American dream.")
]