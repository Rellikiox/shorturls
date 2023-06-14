"""App entrypoint for API endpoints"""

from contextlib import asynccontextmanager

import fastapi
from app import api, models, redirects
from fastapi.middleware import cors


@asynccontextmanager
async def lifespan(app_: fastapi.FastAPI):
    database_ = app_.state.database
    if not database_.is_connected:
        await database_.connect()

    yield

    database_ = app_.state.database
    if database_.is_connected:
        await database_.disconnect()


origins = ["http://localhost", "http://local.api"]


app = fastapi.FastAPI(lifespan=lifespan)
app.state.database = models.database
app.include_router(api.router)
app.include_router(redirects.router)

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
