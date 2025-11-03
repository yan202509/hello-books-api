# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "1984", "A dystopian novel by George Orwell."),
#     Book(2, "To Kill a Mockingbird", "A novel by Harper Lee about racial injustice."),
#     Book(3, "The Great Gatsby", "A novel by F. Scott Fitzgerald about the American dream.")
# ]



from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

    @classmethod
    def from_dict(cls, book_data):
        new_book = cls(title=book_data["title"],
                       description=book_data["description"])
        # We could also use `Book` in place of the `cls` keyword  
        # The following declaration is equivalent to the one above
        # new_book = Book(title=book_data["title"],
        #                 description=book_data["description"])

        return new_book
    
        # indented under the Book class definition
    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict