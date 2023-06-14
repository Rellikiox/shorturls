"""Module to handle redirecting reqeusts to short links to their destinations"""


import fastapi
from http import HTTPStatus
from app import models


router = fastapi.APIRouter()


@router.get("/{short_url:path}")
async def routes(short_url: str):
    target_url = await models.get_original_url(short_url)
    if target_url:
        return fastapi.responses.RedirectResponse(
            target_url, status_code=HTTPStatus.MOVED_PERMANENTLY
        )
    else:
        raise fastapi.HTTPException(status_code=404, detail="Resource not found")
