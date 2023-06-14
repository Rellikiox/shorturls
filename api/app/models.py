"""Short URL models"""

import datetime
import hashids

import databases
import ormar
import sqlalchemy
from app import config

database = databases.Database(config.db_server)
metadata = sqlalchemy.MetaData()

id_hasher = hashids.Hashids(salt=config.hashids_salt, min_length=6)


class ShortURL(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    url: str = ormar.Text()
    short_url: str = ormar.Text(nullable=True)
    created_on: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)


@ormar.post_save(ShortURL)
async def add_short_url_to_entity(sender, instance: ShortURL, **kwargs):
    instance.short_url = id_hasher.encode(instance.id)
    await instance.update()


async def create_short_url(url: str) -> str:
    entity = await ShortURL(url=url).save()
    return entity.short_url


async def get_original_url(short_url: str) -> str | None:
    db_id = id_hasher.decode(short_url)
    if not db_id:
        return None
    entity = await ShortURL.objects.get(ShortURL.id == db_id[0])
    return entity.url if entity and entity.url else None
