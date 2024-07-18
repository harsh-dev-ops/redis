import time
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache


from app.database.redis.models import Author


router  = APIRouter()

@router.get('')
@cache(expire=5)
async def list_authors():
    time.sleep(2)
    authors = await Author.all_pks()
    return [await Author.get(pk=pk) async for pk in authors]

@router.get('/{pk}')
async def get_author(pk: str):
    return await Author.get(pk=pk)


@router.post('/')
async def create_author(author: Author):
    return await author.save()

@router.delete('/{pk}')
async def delete_author(pk: str):
    return await Author.delete(pk=pk)