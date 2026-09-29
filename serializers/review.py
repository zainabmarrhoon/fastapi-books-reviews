from pydantic import BaseModel

class ReviewSerializer(BaseModel):
    content: str
    rating: int
    user_id: int
    book_id: int

class ReviewResponseSerializer(ReviewSerializer):
    id: int