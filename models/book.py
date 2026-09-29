from sqlalchemy import Column, String
from .base import BaseModel

class BookModel(BaseModel):
    __tablename__ = "books"

    title = Column(String, nullable=False)
    author = Column(String, nullable=False)