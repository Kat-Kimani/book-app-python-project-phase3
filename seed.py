# seeds.py

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, Author, Genre, Borrower, Review, borrowed_books

if __name__ == "__main__":
    engine = create_engine("sqlite:///books.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Book).delete()
    session.query(Author).delete()
    session.query(Genre).delete()
    session.query(Borrower).delete()
    session.query(Review).delete()

    fake = Faker()


def create_fake_books(num_books):
    for _ in range(num_books):
        title = fake.sentence(nb_words=3)
        description = fake.paragraph()
        book = Book(title=title, description=description)
        session.add(book)


def create_fake_authors(num_authors):
    for _ in range(num_authors):
        name = fake.name()
        author = Author(name=name)
        session.add(author)


def create_fake_genres(num_genres):
    for _ in range(num_genres):
        name = fake.word()
        genre = Genre(name=name)
        session.add(genre)


def create_fake_borrowers(num_borrowers):
    for _ in range(num_borrowers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        borrower = Borrower(first_name=first_name, last_name=last_name)
        session.add(borrower)


def create_fake_reviews(num_reviews):
    books = session.query(Book).all()
    borrowers = session.query(Borrower).all()

    for _ in range(num_reviews):
        star_rating = random.randint(1, 5)
        comment = fake.paragraph()
        book = random.choice(books)
        borrower = random.choice(borrowers)
        review = Review(star_rating=star_rating, comment=comment)
        review.book = book
        review.borrower = borrower
        session.add(review)


# Generate the fake data
create_fake_books(25)
create_fake_authors(7)

create_fake_genres(4)
create_fake_borrowers(10)
create_fake_reviews(40)

# Commit the changes to the database
session.commit()
