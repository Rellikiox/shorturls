"""App entrypoint for API endpoints"""

from contextlib import asynccontextmanager

import fastapi
from app import api, models, redirects


@asynccontextmanager
async def lifespan(app_: fastapi.FastAPI):
    database_ = app_.state.database
    if not database_.is_connected:
        await database_.connect()

    yield

    database_ = app_.state.database
    if database_.is_connected:
        await database_.disconnect()


app = fastapi.FastAPI(lifespan=lifespan)
app.state.database = models.database
app.include_router(api.router)
app.include_router(redirects.router)
