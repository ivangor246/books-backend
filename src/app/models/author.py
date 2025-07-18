from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .association import book_author_association
from .base import BaseModel, str_100

if TYPE_CHECKING:
    from .book import BookModel


class AuthorModel(BaseModel):
    __tablename__ = 'authors'

    name: Mapped[str_100]
    image_url: Mapped[str]

    books: Mapped[list[BookModel]] = relationship(
        secondary=book_author_association,
        back_populates='authors',
    )
