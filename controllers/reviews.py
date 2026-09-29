from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.review import ReviewModel
from models.user import UserModel
from models.book import BookModel
from serializers.review import ReviewSerializer, ReviewResponseSerializer
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/reviews", response_model=list[ReviewResponseSerializer])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(ReviewModel).all()

@router.post("/reviews", response_model=ReviewResponseSerializer)
def create_review(
    review: ReviewSerializer,
    db: Session = Depends(get_db),
    user: UserModel = Depends(get_current_user)
):
    book = db.query(BookModel).filter(BookModel.id == review.book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    new_review = ReviewModel(
        content=review.content,
        rating=review.rating,
        user_id=user.id,
        book_id=review.book_id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

@router.get("/reviews/{review_id}", response_model=ReviewResponseSerializer)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review

@router.put("/reviews/{review_id}", response_model=ReviewResponseSerializer)
def update_review(review_id: int, review: ReviewSerializer, db: Session = Depends(get_db)):
    existing_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")

    existing_review.content = review.content
    existing_review.rating = review.rating
    existing_review.user_id = review.user_id
    existing_review.book_id = review.book_id

    db.commit()
    db.refresh(existing_review)

    return existing_review

@router.delete("/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}