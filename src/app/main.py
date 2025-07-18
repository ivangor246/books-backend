from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get('/')
    def hello():
        return 'Hello'

    return app
