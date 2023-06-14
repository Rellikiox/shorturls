"""Posts API endpoints"""

import fastapi
from app import models, schemas
from app.config import config
import validators

router = fastapi.APIRouter(prefix="/api/v1")


@router.get("/healthcheck")
async def healthcheck() -> dict:
    return {"service": "short-url", "status": "healthy"}


@router.post("/shorten-url")
async def create_post(body: schemas.ShortenURLRequest) -> schemas.ShortenURLResponse:
    short_url = await models.create_short_url(body.url)
    short_url = f"{config.short_url_host}/{short_url}"
    return schemas.ShortenURLResponse(url=body.url, short_url=short_url)


@router.get("/validate-url")
async def validate_url(
    query: schemas.ValidateURLRequest = fastapi.Depends(),
) -> schemas.ValidateURLResponse:
    is_valid = bool(validators.url(query.url))
    return schemas.ValidateURLResponse(url=query.url, is_valid=is_valid)
