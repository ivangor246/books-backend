from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .association import book_genre_association
from .base import BaseModel, str_50

if TYPE_CHECKING:
    from .book import BookModel


class GenreModel(BaseModel):
    __tablename__ = 'genres'

    name: Mapped[str_50]

    books: Mapped[list[BookModel]] = relationship(
        secondary=book_genre_association,
        back_populates='genres',
    )
