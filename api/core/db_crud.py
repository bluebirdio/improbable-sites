from datetime import datetime

import shortuuid
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import db

from api.core.tables import TextIdentified


def db_process_input(data_in, target=None):
    processed = {}
    data = data_in.dict()
    if target is not None:
        target_data = jsonable_encoder(target)
    else:
        target_data = {}
    for column, value in data.items():
        # Passing id in as the first value causes its setter to fire before there's a name field to utilize
        if column is "id" and value is None:
            continue
        elif column not in target_data.keys() or target_data[column] != value:
            processed[column] = value

    if bool(processed):
        processed["changed"] = datetime.utcnow()

    return processed


def query(model, order_by="name", **kwargs):
    with db():
        q = db.session.query(model).order_by(order_by)

    for key, val in kwargs.items():
        field = getattr(model, key)
        if field is not None:
            filter_value = field == val  # compute expression
            q = q.filter(filter_value)

    return q.all()


def get_or_error(model, item_id, detail="Item not found", query_filter=None):
    item = db_get(model, item_id, query_filter)
    if item is None:
        raise HTTPException(status_code=404, detail=detail)
    return item


def db_get(model, item_id, query_filter=None):
    with db():
        q = db.session.query(model)

    if item_id is int:
        q = q.filter(model.pk == item_id)
    elif issubclass(model, TextIdentified):
        q = q.filter(model._id == item_id)
    else:
        item_uuid = shortuuid.decode(item_id)
        if item_uuid.version is None:
            return None
        else:
            q = q.filter(model.uuid == item_uuid)
    if query_filter is not None:
        q = q.filter(query_filter)

    return q.one_or_none()


def get_by_name(model, item_name):
    with db():
        return db.session.query(model).filter(model.name == item_name).one_or_none()


def create(model, data_in):
    data = db_process_input(data_in)
    item = model(**data)

    validate_create(model, item)
    return db_create(item)


def validate_create(model, item):
    # If id exists (TextIdentified models) verify its uniqueness.
    if item.id is not None:
        if db_get(model, item.id):
            raise HTTPException(422, "ID already exists.")


def db_create(item):
    with db():
        db.session.add(item)
        db.session.commit()
        db.session.refresh(item)
    return item


def update(model, item_id, data_in):
    data = db_process_input(data_in)
    item = get_or_error(model, item_id)
    for column, value in data.items():
        setattr(item, column, value)

    validate_update(model, item)
    db_update(item)


def validate_update(model, item):
    pass


def db_update(item):
    with db():
        db.session.commit()
        db.session.refresh(item)
    return item


def delete(model, item_id):
    item = get_or_error(model, item_id)
    db_delete(item)


def db_delete(item):
    with db():
        db.session.delete(item)
        db.session.commit()
    return
