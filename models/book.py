from sqlalchemy import Column, Integer, String
from .base import BaseModel

class BookModel(BaseModel):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)