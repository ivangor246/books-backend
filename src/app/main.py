from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.config import config
from app.core.lifespan import lifespan


def create_app() -> FastAPI:
    app = FastAPI(
        title=config.TITLE,
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        default_response_class=JSONResponse,
        lifespan=lifespan,
    )

    return app
