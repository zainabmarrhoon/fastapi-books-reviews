from sqlalchemy.orm import sessionmaker
from config.environment import DATABASE_URL
from sqlalchemy import create_engine
from models.base import Base
from models.user import UserModel
from models.book import BookModel
from models.review import ReviewModel

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")

    db = SessionLocal()

    user = UserModel(
        username="zainab",
        email="zainab@example.com"
    )
    user.set_password("password123")

    book = BookModel(
        title="Python Basics",
        author="John Smith"
    )

    db.add(user)
    db.add(book)
    db.commit()

    review = ReviewModel(
        content="Very useful book!",
        rating=5,
        user_id=user.id,
        book_id=book.id
    )

    db.add(review)
    db.commit()

    db.close()

    print("Database seeding complete!")

except Exception as e:
    print("An error occurred:", e)