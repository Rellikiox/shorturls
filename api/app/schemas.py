"""Schemas for the API endpoints"""

import pydantic


class ShortenURLRequest(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to shorten")


class ShortenURLResponse(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to shorten")
    short_url: str = pydantic.Field(title="The shortened URL")


class ValidateURLRequest(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to validate")


class ValidateURLResponse(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL that was validated")
    is_valid: bool = pydantic.Field(title="Wether the URL is valid")
