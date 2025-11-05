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



# app/models/book.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

# we're going to make the Author relationship optional on the Book model, 
# primarily to simplify managing our existing Book data that has no author. 

# author is parent, book is child

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
    author: Mapped[Optional["Author"]] = relationship(back_populates="books")

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        if self.author:
            book_as_dict["author"] = self.author.name

        return book_as_dict
    
    @classmethod
    def from_dict(cls, book_data):
        # Use .get() to fetch values that could be undefined to avoid raising an error

        author_id = book_data.get("author_id")

        new_book = cls(
            title=book_data["title"],
            description=book_data["description"],
            author_id=author_id
        )

        return new_book


