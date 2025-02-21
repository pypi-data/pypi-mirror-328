from .db import WikidataEntityLabel, WikidataClaim
from .labels import lookup_label


def get_target_label(t):
    return lookup_label(t.target_entity)


def get_target_label_and_id(t):
    eid = t.target_entity
    label = lookup_label(eid)
    return {
        'id': eid,
        'label': label
    }


def get_target_value(claim):
    return claim.body


def get_target_text_value(claim):
    return (
        claim.body
        .get('mainsnak', {})
        .get('datavalue', {})
        .get('value', {})
        .get('text')
    )


def default_agg(x):
    return x


def gather(source_entity, prop_id, map_fn, agg_fn):
    claim = WikidataClaim.select().where(
        WikidataClaim.source_entity == source_entity,
        WikidataClaim.property_id == prop_id,
    )

    if map_fn is None:
        map_fn = get_target_label

    if agg_fn is None:
        agg_fn = default_agg

    return agg_fn([map_fn(c) for c in claim])


def fetch(name, prop_id, map_fn=None, agg_fn=None):
    return (name, prop_id, map_fn, agg_fn)


def gather_all(source_entity, cfg):
    item = {}
    for (name, prop_id, map_fn, agg_fn) in cfg:
        item[name] = gather(source_entity, prop_id, map_fn, agg_fn)
    return item
