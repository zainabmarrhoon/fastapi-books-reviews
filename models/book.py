from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel

class BookModel(BaseModel):
    __tablename__ = "books"

    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    reviews = relationship("ReviewModel", back_populates="book")