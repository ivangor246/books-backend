from datetime import datetime
from decimal import Decimal
from typing import Annotated

from sqlalchemy import Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry

str_1 = Annotated[str, 1]
str_50 = Annotated[str, 50]
str_100 = Annotated[str, 100]

num_4_2 = Annotated[Decimal, (4, 2)]
num_8_2 = Annotated[Decimal, (8, 2)]
num_12_2 = Annotated[Decimal, (12, 2)]


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_available: Mapped[bool] = mapped_column(default=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    registry = registry(
        type_annotation_map={
            str_1: String(1),
            str_50: String(50),
            str_100: String(100),
            num_4_2: Numeric(4, 2),
            num_8_2: Numeric(8, 2),
            num_12_2: Numeric(12, 2),
        }
    )
