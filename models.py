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


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    description = Column(String(), nullable=True)

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}')"
