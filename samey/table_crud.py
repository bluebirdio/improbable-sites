from datetime import datetime

import shortuuid
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError

from samey.tables import TextIdentified
from sites.settings import DATABASE_URL


def db_process_input(data_in, target=None):
    target_data = {} if target is None else jsonable_encoder(target)

    processed = {}
    for column, value in data_in.dict().items():
        if column not in target_data.keys() or target_data[column] != value:
            processed[column] = value

    return processed


def query(model, order_by="name", **kwargs):
    with db():
        q = db.session.query(model).order_by(order_by)


    return q.all()


def get_or_error(model, item_id, detail="Item not found", **kwargs):
    with db():
        item = db_get(model, id=item_id, **kwargs)
        if item is None:
            raise HTTPException(status_code=404, detail=detail)
        return item


def exists_or_error(model, item_id, detail="Item not found", **kwargs):
    if not exists(model, id=item_id, **kwargs):
        raise HTTPException(status_code=404, detail=detail)
    else:
        return True


def item_query(q, model, id=None, **kwargs):
    if id is int:
        q = q.filter(model.pk == id)
    elif issubclass(model, TextIdentified):
        q = q.filter(model.id == id)
    elif id is not None:
        item_uuid = shortuuid.decode(id)
        if item_uuid.version is None:
            return None
        else:
            q = q.filter(model.uuid == item_uuid)

    for key, val in kwargs.items():
        field = getattr(model, key)
        if field is not None:
            filter_value = field == val  # compute expression
            q = q.filter(filter_value)

    return q


def exists(model, id=None, **kwargs):
    with db():
        q = db.session.query(model)
        q = item_query(q, model, id=id, **kwargs)

        return db.session.query(q.exists()).scalar()


def db_get(model, id=None, **kwargs):
    with db():
        q = db.session.query(model)
        q = item_query(q, model, id=id, **kwargs)

        item = q.one_or_none()

        # Detach from the db session to support threading. Must use session.add() before running ORM operations.
        if item is not None:
            db.session.expunge(item)
        return item


def create(model, data_in):
    data = db_process_input(data_in)
    item = model(**data)

    with db():
        try:
            db.session.add(item)
            db.session.commit()
            db.session.refresh(item)
        except IntegrityError:
            raise HTTPException(422, "ID already exists.")
    return item


def update(model, item_id, data_in):
    data = db_process_input(data_in)
    if id in data and data["id"] != item_id:
        raise HTTPException(status_code=422, detail="Can not change ID.")

    with db():
        # Enforce referential integrity for Sqlite
        if DATABASE_URL[:6] == "sqlite":
            db.session.execute("PRAGMA foreign_keys = ON")

        item = get_or_error(model, item_id)
        for column, value in data.items():
            if value != getattr(item, column):
                setattr(item, "changed", datetime.utcnow())
                setattr(item, column, value)

        db.session.add(item)
        try:
            db.session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=422,
                detail="This update would break references. Not performing.",
            )

        db.session.refresh(item)
        return item


def delete(model, item_id):
    item = get_or_error(model, item_id)

    with db():
        # Enforce referential integrity for Sqlite
        if DATABASE_URL[:6] == "sqlite":
            db.session.execute("PRAGMA foreign_keys = ON")
        try:
            db.session.query(model).filter(model.pk == item.pk).delete()
            db.session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=422,
                detail="Can't delete this item because it is still being referenced.",
            )
