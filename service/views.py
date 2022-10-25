import json

from pydantic import BaseModel
from typing import List
from sqlalchemy import select
from fastapi import Request, Path, HTTPException

from .app import app
from .version import __version__


class Batch(BaseModel):
    list_of_items: List[int]


def stringify(iterable):
    """Dynamically transforms an iterable into SQL-friendly format"""
    assert hasattr(iterable, '__iter__'), "Need to pass an iterable"
    assert len(iterable) >= 1, "Iterable has to be non-empty"
    if len(iterable) > 1:
        return str(tuple(iterable))
    return str(tuple(iterable))[:-2]+')'


MICROSERVICE_ID = 1


@app.get("/version")
async def version():
    """It shows the actual version of the microservice."""
    return {'version': __version__}


@app.get("/process_one/{item_id}")
async def process_one(item_id: int = Path(..., title="item")):
    """Gets all items in the same cluster"""
    item = [item_id]
    result = await my_query(item)
    if result is None:
        raise HTTPException(status_code=404, detail=item)
    return result


@app.post("/process_batch")
async def process_batch(item: itemBatch):
    """Gets all items affiliated with items in batch"""
    result = await call_to_database(item.list_of_items)
    if result is None:
        raise HTTPException(status_code=404, detail=item)
    return result
