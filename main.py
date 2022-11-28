from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import init_db
from routers import router


def create_app() -> FastAPI:
    app = FastAPI(
        contact={
            "name": " Yeren Kalibek",
            "email": "yerenn22@gmail.com",
        },
        description="""
        Backend application for publishing postsuser roles, moderator/administrator confirmation and cron tasks""",
        docs_url="/",
        title="Post App",
        version="0.2.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app


app = create_app()


@app.on_event("startup")
async def startup():
    init_db()
