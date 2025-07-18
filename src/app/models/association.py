from sqlalchemy import Column, ForeignKey, Table

from .base import BaseModel

book_author_association = Table(
    'book_author_association',
    BaseModel.metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('author_id', ForeignKey('authors.id')),
)


book_genre_association = Table(
    'book_genre_association',
    BaseModel.metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('genre_id', ForeignKey('genres.id')),
)
