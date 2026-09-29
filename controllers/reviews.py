from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.review import ReviewModel
from serializers.review import ReviewSerializer, ReviewResponseSerializer

router = APIRouter()

@router.get("/reviews", response_model=list[ReviewResponseSerializer])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(ReviewModel).all()

@router.post("/reviews", response_model=ReviewResponseSerializer)
def create_review(review: ReviewSerializer, db: Session = Depends(get_db)):
    new_review = ReviewModel(
        content=review.content,
        rating=review.rating,
        user_id=review.user_id,
        book_id=review.book_id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review