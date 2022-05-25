import pytest
from fundb import fundb
from fundb.database import Database, Collection, Document

def test_create_db():
    db = fundb()
    assert isinstance(db, Database)

def test_select_collection():
    db = fundb()
    coll = db.select("collname")
    assert isinstance(coll, Collection)
    assert coll.name == "collname"

def test_select_collection_magic():
    db = fundb()
    coll = db.collname
    assert isinstance(coll, Collection)

def test_select_collection_name_magic():
    db = fundb()
    coll = db.collname
    assert coll.name == "collname"

def test_collection_size():
    db = fundb()
    coll = db.collname

    for i in range(5):
        coll.insert({"name": "x"})
    assert coll.size == 5