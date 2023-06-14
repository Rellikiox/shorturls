import os


class Config:
    db_server: str = os.environ.get(
        "DB_SERVER",
        "postgresql+psycopg2://urls_admin:urls_password@localhost:5432/urls",
    )
    hashids_salt: str = os.environ.get("HASHIDS_SALT", "")
    short_url_host: str = os.environ.get("SHORT_URL_HOST", "localhost")


config = Config()
