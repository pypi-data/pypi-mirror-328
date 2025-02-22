from functools import lru_cache
from .db import WikidataEntityEnSiteLink


@lru_cache(maxsize=1024 + 30)  # Adjust size as needed
def lookup_label(entity):
    item = WikidataEntityEnSiteLink.get_or_none(WikidataEntityEnSiteLink.entity_id == entity)
    return item.title if item else entity
