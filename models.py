from sqlalchemy import (
    create_engine,
    ForeignKey,
    Column,
    Integer,
    String,
    MetaData,
    Table,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///books.db", echo=True)
Base = declarative_base()


borrowed_books = Table(
    "borrowed_books",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("borrower_id", Integer, ForeignKey("borrowers.id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    description = Column(String(), nullable=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    borrowers = relationship(
        "Borrower", secondary=borrowed_books, back_populates="books"
    )

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}')"


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)

    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    books = relationship("Book", back_populates="genre")


class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    books = relationship("Book", secondary=borrowed_books, back_populates="borrowers")

    def __repr__(self):
        return f"Borrower(id={self.id},first_name={self.first_name},last_name={self.last_name}, title='{self.title}')"


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    comment = Column(String(50), nullable=True)

    def __repr__(self):
        return f"Review(id={self.id},star_rating={self.star_rating},comment={self.comment})"
