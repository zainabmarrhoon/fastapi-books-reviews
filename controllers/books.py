from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.book import BookModel
from serializers.book import BookResponseSerializer

router = APIRouter()

@router.get("/books", response_model=list[BookResponseSerializer])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()