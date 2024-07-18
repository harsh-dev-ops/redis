import time
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from app.database.redis.models import Book, Author
from app.cache.coder import ORJsonCoder
from app.cache.key_builder import request_key_builder

router  = APIRouter()

@router.get('')
@cache(expire=60, coder=ORJsonCoder, key_builder=request_key_builder)
async def list_books():
    time.sleep(5)
    books = await Book.all_pks()
    result = []
    async for pk in books:
        book = await Book.get(pk=pk)
        author = await Author.get(pk=book.author)
        book.author = author
        result.append(book)
    return result

@router.get('/{pk}')
async def get_book(pk: str):
    return await Book.get(pk=pk)


@router.post('/')
async def create_book(book: Book):
    return await book.save()


@router.delete('/{pk}')
async def delete_book(pk: str):
    return await Book.delete(pk=pk)