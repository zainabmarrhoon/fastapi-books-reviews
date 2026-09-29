from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from controllers.users import router as UsersRouter
from controllers.books import router as BooksRouter

app = FastAPI()

app.include_router(UsersRouter, prefix='/api')
app.include_router(BooksRouter, prefix='/api')

@app.get('/')
def home():
    return {'message': 'Home Page'}