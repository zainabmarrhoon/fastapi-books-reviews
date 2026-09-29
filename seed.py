from sqlalchemy.orm import sessionmaker
from config.environment import DATABASE_URL
from sqlalchemy import create_engine
from models.base import Base
from models.user import UserModel
from models.book import BookModel

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")

    db = SessionLocal()

    book = BookModel(
        title="Python Basics",
        author="John Smith"
    )

    db.add(book)
    db.commit()

    db.close()

    print("Database seeding complete!")

except Exception as e:
    print("An error occurred:", e)