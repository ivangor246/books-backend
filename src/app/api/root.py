from fastapi import APIRouter

from .book import book_router

ROUTERS = [
    book_router,
]


def get_root_router() -> APIRouter:
    root_router = APIRouter(prefix='/api')

    for router in ROUTERS:
        root_router.include_router(router)

    return root_router
