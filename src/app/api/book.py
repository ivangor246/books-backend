from fastapi import APIRouter

book_router = APIRouter(prefix='/books')


@book_router.get('/')
async def get_books():
    return 'Some books'
