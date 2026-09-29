from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.book import BookModel
from serializers.book import BookSerializer, BookResponseSerializer

router = APIRouter()

@router.get("/books", response_model=list[BookResponseSerializer])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()

@router.post("/books", response_model=BookResponseSerializer)
def create_book(book: BookSerializer, db: Session = Depends(get_db)):
    new_book = BookModel(
        title=book.title,
        author=book.author
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@router.get("/books/{book_id}", response_model=BookResponseSerializer)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(BookModel).filter(BookModel.id == book_id).first()