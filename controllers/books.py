from fastapi import APIRouter, Depends, HTTPException
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
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.put("/books/{book_id}", response_model=BookResponseSerializer)
def update_book(book_id: int, book: BookSerializer, db: Session = Depends(get_db)):
    existing_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    existing_book.title = book.title
    existing_book.author = book.author

    db.commit()
    db.refresh(existing_book)

    return existing_book

@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}