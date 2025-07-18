from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association import book_author_association, book_genre_association
from .base import BaseModel, num_4_2, num_8_2, str_100

if TYPE_CHECKING:
    from .author import AuthorModel
    from .genre import GenreModel


class BookModel(BaseModel):
    __tablename__ = 'books'

    title: Mapped[str_100]
    description: Mapped[str]
    price: Mapped[num_8_2] = mapped_column(CheckConstraint('price >= 0'), default=0)
    rating: Mapped[num_4_2] = mapped_column(CheckConstraint('rating >= 0 AND rating <= 10'), default=0)
    image_url: Mapped[str]
    amount: Mapped[int]

    authors: Mapped[list[AuthorModel]] = relationship(
        secondary=book_author_association,
        back_populates='books',
    )
    genres: Mapped[list[GenreModel]] = relationship(
        secondary=book_genre_association,
        back_populates='books',
    )
