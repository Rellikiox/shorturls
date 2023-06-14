"""Schemas for the API endpoints"""

import pydantic
import validators


class ShortenURLRequest(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to shorten")

    @pydantic.validator("url")
    def url_must_be_valid(cls, value):
        if not validators.url(value):
            raise ValueError("must be a valid URL")
        return value


class ShortenURLResponse(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to shorten")
    short_url: str = pydantic.Field(title="The shortened URL")


class ValidateURLRequest(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL to validate")


class ValidateURLResponse(pydantic.BaseModel):
    url: str = pydantic.Field(title="The URL that was validated")
    is_valid: bool = pydantic.Field(title="Wether the URL is valid")
